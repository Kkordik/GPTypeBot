from classes.Markers import BeginMarker, DotSign, ExclamationSign, QuestionSign, SimpleEndMarker
from config import TELEGRAM_CHAR_LIMIT

texts = {
    "en": {
        "start_text": "Powerful, unique, and free.\nCheck the short guide below before using me or start right now!",
        "see_more_but": "See more..",
        "share": "Hello I use @GPTypeBot, it is very convenient!",
        "guide_but": "guide",
        "start_use_but": "start use"
    },
    "uk": {
        "start_text": "Могутній, унікальний та безкоштовний.\nПереглянь короткий гайд нижче,"
                      " перш ніж користуватися мною, або почни прямо зараз!",
        "see_more_but": "Подробиці..",
        "share": "Привіт, я використовую @GPTypeBot, це дуже зручно!",
        "guide_but": "guide",
        "start_use_but": "start use"
    },
    "ru": {
        "start_text": "Мощный, уникальный и бесплатный.\nПроверь краткий гайд ниже,"
                      " прежде чем использовать меня, или начни прямо сейчас!",
        "see_more_but": "Подробнее..",
        "share": "Привет, я использую @GPTypeBot, это очень удобно!",
        "guide_but": "guide",
        "start_use_but": "start use"
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
        "wrong_marker_use": "Check correctness of marker {}",
        "too_long_query": f"Query is over {TELEGRAM_CHAR_LIMIT} symbols. Telegram limit😢",
        "waiting_time": "Genereting responce tates up to 5s"
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
        "wrong_marker_use": "Перевір правильність маркеру {}",
        "too_long_query": f"Запит більше ніж {TELEGRAM_CHAR_LIMIT} символів. Це ліміт Телеграму😢",
        "waiting_time": "Genereting responce tates up to 5s"
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
        "wrong_marker_use": "Проверь правильность маркера {}",
        "too_long_query": f"Запрос больше {TELEGRAM_CHAR_LIMIT} символов. Это лимит Телеграма😢",
        "waiting_time": "Genereting responce tates up to 5s"
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
                           "<b>'-t-language'</b> is a translate start marker. Translates given text to the specified"
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
    "ru": {
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
                           "<b>'-t-language'</b> is a translate start marker. Translates given text to the specified"
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
    }
}
