from classes.Markers import BeginMarker, DotSign, ExclamationSign, QuestionSign, SimpleEndMarker
from config import TELEGRAM_CHAR_LIMIT

texts = {
    "en": {
        "start_text": "Powerful, unique, and free.\nCheck the short guide below before using me or start right now!\nFeedback: @kkordik",
        "see_more_but": "See more..",
        "buy_subs_but": "Buy now..",
        "share": "Hello I use @GPTypeBot, it is very convenient!",
        "guide_but": "guide",
        "start_use_but": "start use",
        "wait_for_answer": "Please wait♻️"
    },
    "uk": {
        "start_text": "Могутній, унікальний та безкоштовний.\nПереглянь короткий гайд нижче,"
                      " перш ніж користуватися мною, або почни прямо зараз!\nFeedback: @kkordik",
        "see_more_but": "Подробиці..",
        "buy_subs_but": "Придбати..",
        "share": "Привіт, я використовую @GPTypeBot, це дуже зручно!",
        "guide_but": "Гайд",
        "start_use_but": "Почати використовувати",
        "wait_for_answer": "Будь ласка зачекайте♻️"
    },
    "ru": {
        "start_text": "Мощный, уникальный и бесплатный.\nПроверь краткий гайд ниже,"
                      " прежде чем использовать меня, или начни прямо сейчас!\nFeedback: @kkordik",
        "see_more_but": "Подробнее..",
        "buy_subs_but": "Купить..",
        "share": "Привет, я использую @GPTypeBot, это очень удобно!",
        "guide_but": "Гайд",
        "start_use_but": "Начать использовать",
        "wait_for_answer": "Пожалуйста подождите♻️"
    }
}

facts = {
    "en": {
        "start_with_marker":  "Ask or start with marker: '{}'".format(
            "' / '".join([b_marker.marker for b_marker in BeginMarker.__subclasses__()])
        ),

        "end_with_sign":  "Remember query ends with '{}' / '{}' / '{}' / '{}'".format(
                           DotSign.marker,
                           ExclamationSign.marker,
                           QuestionSign.marker,
                           SimpleEndMarker.marker
        ),
        "wrong_marker_use": "Check correctness of marker '{}'",
        "too_long_query": f"Query is over {TELEGRAM_CHAR_LIMIT} symbols. Telegram limit😢",
        "waiting_time": "Generating response takes up to 10 seconds",
        "no_subscription": "This feature is only for paid subscribers",
        "unknown_error": "Sorry, try again"
    },
    "uk": {
        "start_with_marker":  "Запитуй або юзай маркер: '{}'".format(
            "' / '".join([b_marker.marker for b_marker in BeginMarker.__subclasses__()])
        ),
        "end_with_sign": "Пам'ятай, запит закінчується на '{}' / '{}' / '{}' / '{}'".format(
                          DotSign.marker,
                          ExclamationSign.marker,
                          QuestionSign.marker,
                          SimpleEndMarker.marker
        ),
        "wrong_marker_use": "Перевір правильність маркеру '{}'",
        "too_long_query": f"Запит більше ніж {TELEGRAM_CHAR_LIMIT} символів. Це ліміт Телеграму😢",
        "waiting_time": "В середньому відповідь генерується приблизно 10 секунд",
        "no_subscription": "Ця функція тільки для преміум підписників",
        "unknown_error": "Вибач, спробуй ще раз"
    },
    "ru": {
        "start_with_marker": "Спрашивай или юзай маркер: '{}'".format(
            "' / '".join([b_marker.marker for b_marker in BeginMarker.__subclasses__()])
        ),

        "end_with_sign": "Помни, запрос заканчивается на '{}' / '{}' / '{}' / '{}'".format(
                          DotSign.marker,
                          ExclamationSign.marker,
                          QuestionSign.marker,
                          SimpleEndMarker.marker
        ),
        "wrong_marker_use": "Проверь правильность маркера '{}'",
        "too_long_query": f"Запрос больше {TELEGRAM_CHAR_LIMIT} символов. Это лимит Телеграма😢",
        "waiting_time": "В среднем ответ генерируется примерно 10 секунд",
        "no_subscription": "Эта функция только для премиум подписчиков",
        "unknown_error": "Извини, попробуй еще раз"
    }
}

guide_texts = {
    "en": {
        "inline_bot": {
            "description": "It is an inline bot, that means that you can use it in any chat. "
                           "To call the bot simply type @GPTypeBot",
            "button": "Inline bot",
            "examples": []
        },
        "simple_query": {
            "description": "After you've called the bot, type your query, which can be simple or with markers\n\n"
                           "<b>Simple query</b>\n\nIt is a query, that consists of one question or request to the bot,"
                           " the result will be the answer to it.\nMust finish with '.' or '?' or '!'\n\n<i>Generating "
                           "response to the example takes time, please be patient</i>",
            "button": "Simple query",
            "examples": [{"button": "Example", "query": "Why doing sport is healthy?"}]
        },
        "marked_query": {
            "description": "<b>Marked query</b>\n\nIt is a query that consists of one or more simple sub-queries "
                           "separated by start/end markers, the text outside of the markers will be returned in the "
                           "result at the  same positions as it is in the query\nMust finish with ‘.’ or ‘?’ or ‘!’ or"
                           " can finish with end marker ‘-q’ if before is sub-query.\n\nIn the example: '-s' is a "
                           "simple start marker and '-q' is an end marker (about Markers later)",
            "button": "Marked query",
            "examples": [
                {"button": "Example 1", "query": "Here is how to be punctual: -s How to be punctual? -q You must know it!"},
                {"button": "Example 2", "query": "Here is how to be punctual: -s How to be punctual?"}
            ]
        },
        "markers_list": {
            "description": "<b>Markers</b>\n\nMarkers are used to separate sub-queries and to specify its "
                           "handling type.\n\n<b>Begin Markers:</b>\n"
                           "<b>'-s'</b>   is a simple start marker. Doesn't have any specific handling.\n"
                           "<b>'-f'</b>   is a formal start marker. Writes a formal message based on the given theme.\n"
                           "<b>'-p'</b>   is a post start marker. Creates a post based on the given theme and details.\n"
                           "<b>'-t-language'</b>   is a translate start marker. Translates given text to the specified"
                           " language\n"
                           "<b>'-m'</b>   is a mistakes start marker. Corrects mistakes in the given text.\n\n"
                           "<b>End Marker:</b>\n"
                           "<b>'-q'</b>   is a quit end marker. Is used to finish queries and sub-queries.",
            "button": "Markers",
            "examples": [
                {"button": "Example -f", "query": "-f Alex, I am late, sorry, traffic jams!"},
                {"button": "Example -p", "query": "-p We have to stop climate changing or it will kill us!"},
                {"button": "Example -t", "query": "-t-spanish Hi! My name is Max, glad to see you in this chat!"},
                {"button": "Example -m", "query": "-m I have jast told u thet I will continu sleping!"},
                {"button": "Example -q", "query": "-s Give me 5 reasons why should I start exercising -q"},
            ]
        },
        "last_page": {
            "description": "<b>Congrats! You have finished this short guide! Start enjoying the bot!</b>",
            "button": "Finish",
            "examples": []
        }
    },
    "uk": {
        "inline_bot": {
            "description": "Це інлайн-бот, що означає, що ви можете використовувати його в будь-якому чаті. "
                           "Щоб викликати бота, просто введіть @GPTypeBot",
            "button": "Інлайн-бот",
            "examples": []
        },
        "simple_query": {
            "description": "Після виклику бота введіть свій запит, який може бути простим або з маркерами\n\n"
                           "<b>Простий запит</b>\n\nЦе запит, який складається з одного запитання або прохання до бота,"
                           " результатом буде відповідь на нього.\nПовинен закінчуватися на '.' або '?' або '!'\n\n<i>Генерація "
                           "відповіді на приклад займає час, будь ласка, будьте терплячі</i>",
            "button": "Простий запит",
            "examples": [{"button": "Приклад", "query": "Why doing sport is healthy?"}]
        },
        "marked_query": {
            "description": "<b>Запит з маркерами</b>\n\nЦе запит, який складається з одного або кількох простих підзапитів, "
                           "розділених маркерами початку і кінця. Текст поза маркерами буде повернений в результаті на тих же позиціях, "
                           "де він знаходиться в запиті.\nПовинен закінчуватися на ‘.’ або ‘?’ або ‘!’ або "
                           "може закінчуватися маркером кінця ‘-q’, якщо перед ним є підзапит.\n\nУ прикладі: '-s' це "
                           "початковий маркер, а '-q' - кінцевий маркер (докладніше про маркери згодом)",
            "button": "Запит з маркерами",
            "examples": [
                {"button": "Приклад 1", "query": "Here is how to be punctual: -s How to be punctual? -q You must know it!"},
                {"button": "Приклад 2", "query": "Here is how to be punctual: -s How to be punctual?"}
            ]
        },
        "markers_list": {
                "description": "<b>Маркери</b>\n\nМаркери використовуються для розділення підзапитів та вказівки типу їх обробки.\n\n<b>Початкові маркери:</b>\n"
                               "<b>'-s'</b> це простий початковий маркер. Не має конкретної обробки.\n"
                               "<b>'-f'</b> це формальний початковий маркер. Створює формальне повідомлення на основі вказаної теми.\n"
                               "<b>'-p'</b> це пост-початковий маркер. Створює пост на основі вказаної теми та деталей.\n"
                               "<b>'-t-мова'</b> це початковий маркер перекладу. Перекладає вказаний текст на вказану мову.\n"
                               "<b>'-m'</b> це початковий маркер помилок. Виправляє помилки у вказаному тексті.\n\n"
                               "<b>Кінцевий маркер:</b>\n"
                               "<b>'-q'</b> це кінцевий маркер виходу. Використовується для завершення запитів та підзапитів.",
                "button": "Маркери",
                "examples": [
                        {"button": "Приклад -f", "query": "-f Alex, I am late, sorry, traffic jams!"},
                        {"button": "Приклад -p", "query": "-p We have to stop climate changing or it will kill us!"},
                        {"button": "Приклад -t", "query": "-t-spanish Hi! My name is Max, glad to see you in this chat!"},
                        {"button": "Приклад -m", "query": "-m I have jast told u thet I will continu sleping!"},
                        {"button": "Приклад -q", "query": "-s Give me 5 reasons why should I start exercising -q"},
                ]
        },
        "last_page": {
                "description": "<b>Вітаю! Ви завершили цей короткий посібник! Починайте користуватися ботом!</b>",
                "button": "Завершити",
                "examples": []
        }

    },
    "ru": {
        "inline_bot": {
            "description": "Это инлайн-бот, то есть вы можете использовать его в любом чате. Чтобы вызвать бота, "
                           "просто введите @GPTypeBot",
            "button": "Инлайн-бот",
            "examples": []
        },
        "simple_query": {
            "description": "После вызова бота введите свой запрос, который может быть простым или с маркерами\n\n"
                           "<b>Простой запрос</b>\n\nЭто запрос, который состоит из одного вопроса или запроса к боту, "
                           "результатом будет ответ на него. \nДолжен заканчиваться на '.' или '?' или '!'\n\n<i>Формирование "
                           "ответа на пример занимает время, пожалуйста, будьте терпеливы</i>",
            "button": "Простой запрос",
            "examples": [{"button": "Пример", "query": "Why doing sport is healthy?"}]
        },
        "marked_query": {
            "description": "<b>Запрос с маркерами</b>\n\nЭто запрос, который состоит из одного или нескольких "
                           "простых подзапросов, разделенных маркерами начала и конца, текст за пределами маркеров "
                           "будет возвращен в результате на тех же позициях, что и в запросе.\nДолжен заканчиваться на"
                           " '.' или '?' или '!' или может заканчиваться на маркер конца '-q', если перед ним есть подзапрос. \n\n"
                           "В примере: '-s' - это простой маркер начала, а '-q' - маркер конца (о маркерах позже)",
            "button": "Запрос с маркерами",
            "examples": [
                {"button": "Пример 1", "query": "Here is how to be punctual: -s How to be punctual? -q You must know it!"},
                {"button": "Пример 2", "query": "Here is how to be punctual: -s How to be punctual?"}
            ]
        },
        "markers_list": {
            "description": "<b>Маркеры</b>\n\nМаркеры используются для разделения подзапросов и указания его типа "
                           "обработки.\n\n<b>Маркеры начала:</b>\n"
                           "<b>'-s'</b>   это простой маркер начала. Не имеет определенной обработки.\n"
                           "<b>'-f'</b>   это формальный маркер начала. Создает формальное сообщение на основе указанной темы.\n"
                           "<b>'-p'</b>   это маркер начала поста. Создает пост на основе указанной темы и деталей.\n"
                           "<b>'-t-язык'</b> это маркер начала перевода. Переводит заданный текст на указанный язык.\n"
                           "<b>'-m'</b>   это маркер начала исправления ошибок. Исправляет ошибки в заданном тексте.\n\n"
                           "<b>Маркер конца:</b>\n"
                           "<b>'-q'</b>   это маркер конца запросов и подзапросов.",
            "button": "Маркеры",
            "examples": [
                        {"button": "Пример -f", "query": "-f Alex, I am late, sorry, traffic jams!"},
                        {"button": "Пример -p", "query": "-p We have to stop climate changing or it will kill us!"},
                        {"button": "Пример -t", "query": "-t-spanish Hi! My name is Max, glad to see you in this chat!"},
                        {"button": "Пример -m", "query": "-m I have jast told u thet I will continu sleping!"},
                        {"button": "Пример -q", "query": "-s Give me 5 reasons why should I start exercising -q"},
            ],
        },
        "last_page": {
            "description": "<b>Поздравляем! Вы закончили этот короткий гид! Начинайте пользоваться ботом!</b>",
            "button": "Закончить",
            "examples": []
        }
    }
}
