from builtins import list
import tiktoken
import aiohttp
from config import DEFAULT_TOKEN_NUM, MAX_TOKEN_NUM, BOT_ROLE, USER_ROLE
from classes.MainClasses import QueryDb
from typing import List


class PrevMessages:
    def __init__(self, short_answers: bool = True):
        self.short_answers = short_answers
        self.__messages_list: list = []

    def get_messages_list(self) -> list:
        if self.short_answers:
            salt = " Answer shortly."
        else:
            salt = ""
        return [{"role": "system", "content": f"You are a helpful {BOT_ROLE}.{salt}"}] + self.__messages_list

    def count_tokens(self, model="gpt-3.5-turbo-0301"):
        """Returns the number of tokens used by a list of messages."""
        try:
            encoding = tiktoken.encoding_for_model(model)
        except KeyError:
            print("Warning: model not found. Using cl100k_base encoding.")
            encoding = tiktoken.get_encoding("cl100k_base")
        if model == "gpt-3.5-turbo":
            print("Warning: gpt-3.5-turbo may change over time. Returning num tokens assuming gpt-3.5-turbo-0301.")
            return num_tokens_from_messages(messages, model="gpt-3.5-turbo-0301")
        elif model == "gpt-4":
            print("Warning: gpt-4 may change over time. Returning num tokens assuming gpt-4-0314.")
            return num_tokens_from_messages(messages, model="gpt-4-0314")
        elif model == "gpt-3.5-turbo-0301":
            tokens_per_message = 4  # every message follows <im_start>{role/name}\n{content}<im_end>\n
            tokens_per_name = -1  # if there's a name, the role is omitted
        elif model == "gpt-4-0314":
            tokens_per_message = 3
            tokens_per_name = 1
        else:
            raise NotImplementedError(
                f"""num_tokens_from_messages() is not implemented for model {model}. See https://github.com/openai/openai-python/blob/main/chatml.md for information on how messages are converted to tokens.""")
        num_tokens = 0
        for message in self.get_messages_list():
            num_tokens += tokens_per_message
            for key, value in message.items():
                num_tokens += len(encoding.encode(value))
                if key == "name":
                    num_tokens += tokens_per_name
        num_tokens += 2  # every reply is primed with <im_start>assistant
        return num_tokens

    def add_previous_message(self, message: str, user: str, default_token_num: int, max_token_num: int) -> bool:
        self.__messages_list.insert(0, {"role": user, "content": message})
        if self.count_tokens() + default_token_num < max_token_num:
            return True
        else:
            self.del_last_message()
            return False

    def add_last_query(self, query_text: str, user: str, max_token_num: int) -> int:
        """
        Returns approximately left token free space
        """
        self.__messages_list.append({"role": user, "content": query_text})
        return max_token_num - self.count_tokens() - 1

    def del_last_message(self):
        self.__messages_list.pop(0)

    def add_previous_queries(self, prev_queries_db: List[QueryDb], default_token_num: int = DEFAULT_TOKEN_NUM,
                             max_token_num: int = MAX_TOKEN_NUM):
        for prev_query_db in prev_queries_db:
            answer_is_added = self.add_previous_message(message=prev_query_db.answer,
                                                        user=BOT_ROLE,
                                                        default_token_num=default_token_num,
                                                        max_token_num=max_token_num)
            query_is_added = self.add_previous_message(message=prev_query_db.query,
                                                       user=USER_ROLE,
                                                       default_token_num=default_token_num,
                                                       max_token_num=max_token_num)
            # Avoid not answered questions or answers without questions
            if query_is_added != answer_is_added:
                self.del_last_message()
                break
            elif not answer_is_added and not query_is_added:
                break


class GPT:
    session = aiohttp.ClientSession()

    def __init__(self, token: str, url: str= None, model: str = None, prompt: str = None, edit_input: str = None,
                 instruction: str = None, data: dict = None, headers: dict = None, response: dict = None,
                 messages: PrevMessages = None):
        self.url: str = url
        self.model: str = model
        self.prompt: str = prompt
        self.edit_input: str = edit_input
        self.instruction: str = instruction
        self.max_tokens: int = 100
        self.temperature: int = 1
        self.n: int = 1
        self.echo: bool = False
        self.data: dict = data
        self.headers: dict = headers
        self.response: dict = response
        self.messages: PrevMessages = messages
        self.token = token

    async def completion(self, prompt: str, max_tokens: int = None, model: str = None, temperature: int = None,
                         n: int = None, echo: bool = None) -> str:
        self.url = "https://api.openai.com/v1/completions"
        self.prompt = prompt
        self.model = model or "text-davinci-003"
        self.max_tokens = max_tokens or DEFAULT_TOKEN_NUM
        self.temperature = temperature or 1
        self.n = n or 1
        self.echo = echo or False

        self.data = {
            "model": self.model,
            "prompt": self.prompt,
            "max_tokens": self.max_tokens,
            "temperature": self.temperature,
            "n": self.n,
        }
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }
        response = await self.session.post(self.url, headers=self.headers, json=self.data)
        self.response = await response.json()
        return self.response['choices'][0]['text']

    async def edit(self, edit_input: str, instruction: str, model: str = None, temperature: int = None,
                   n: int = None) -> str:
        self.url = "https://api.openai.com/v1/edits"
        self.edit_input = edit_input
        self.instruction = instruction
        self.model = model or "text-davinci-edit-001"
        self.temperature = temperature or 1
        self.n = n or 1

        self.data = {
            "model": self.model,
            "input": self.edit_input,
            "instruction": self.instruction,
            "temperature": self.temperature,
            "n": self.n,
        }
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }
        response = await self.session.post(self.url, headers=self.headers, json=self.data)
        self.response = await response.json()
        return self.response['choices'][0]['text']

    async def chat_completion(self, messages: PrevMessages, max_tokens: int = None, temperature: int = None,
                              n: int = None, echo: bool = None):
        self.url = "https://api.openai.com/v1/chat/completions"
        self.model = "gpt-3.5-turbo-0301"
        self.messages: PrevMessages = messages
        self.max_tokens = max_tokens or DEFAULT_TOKEN_NUM
        self.temperature = temperature or 1
        self.n = n or 1
        self.echo = echo or False

        self.data = {
            "model": self.model,
            "messages": self.messages.get_messages_list(),
            "max_tokens": self.max_tokens,
            "temperature": self.temperature,
            "n": self.n,
            "stream": self.echo
        }
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }
        response = await self.session.post(self.url, headers=self.headers, json=self.data)
        self.response = await response.json()
        return self.response['choices'][0]['message']['content']
