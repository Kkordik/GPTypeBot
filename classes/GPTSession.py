from builtins import list

import aiohttp
from config import DEFAULT_TOKEN_NUM

BOT_ROLE = "assistant"


class PrevMessages:
    messages_list: list

    def __init__(self):
        self.messages_list = [{"role": "system", "content": f"You are a helpful {BOT_ROLE}."}]

    def add_message(self, message: str, user: str = BOT_ROLE):
        self.messages_list.append({"role": user, "content": message})


class GPT:
    url: str
    model: str
    prompt: str
    edit_input: str
    instruction: str
    max_tokens: int = 100
    temperature: int = 1
    n: int = 1
    echo: bool = False
    data: dict
    headers: dict
    response: dict
    messages: PrevMessages

    def __init__(self, token: str):
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
        async with aiohttp.ClientSession() as session:
            async with session.post(self.url, headers=self.headers, json=self.data) as response:
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
        async with aiohttp.ClientSession() as session:
            async with session.post(self.url, headers=self.headers, json=self.data) as response:
                self.response = await response.json()
        return self.response['choices'][0]['text']

    async def chat_completion(self, messages: PrevMessages, max_tokens: int = None, temperature: int = None,
                              n: int = None, echo: bool = None):
        self.url = "https://api.openai.com/v1/chat/completions"
        self.model = "gpt-3.5-turbo"
        self.messages: PrevMessages = messages
        self.max_tokens = max_tokens or DEFAULT_TOKEN_NUM
        self.temperature = temperature or 1
        self.n = n or 1
        self.echo = echo or False

        self.data = {
            "model": self.model,
            "messages": self.messages.messages_list,
            "max_tokens": self.max_tokens,
            "temperature": self.temperature,
            "n": self.n,
            "stream": self.echo
        }
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.url, headers=self.headers, json=self.data) as response:
                self.response = await response.json()
        return self.response['choices'][0]['message']['content']
