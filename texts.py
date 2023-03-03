from classes.Markers import DotSign, ExclamationSign, QuestionSign, SimpleEndMarker

texts = {
    "en": {
        "start_text": "Powerful, unique, and free.\nCheck the short guide below before using me or start right now!",
        "see_more_but": "See more..",
        "share": "Hello I use @GPTypeBot, it is very convenient!"
    },
    "uk": {
        "start_text": "Могутній, унікальний та безкоштовний.\nПереглянь короткий гайд нижче,"
                      " перш ніж користуватися мною, або почни прямо зараз!",
        "see_more_but": "Подробиці..",
        "share": "Привіт, я використовую @GPTypeBot, це дуже зручно!"
    },
    "ru": {
        "start_text": "Мощный, уникальный и бесплатный.\nПроверь краткий гайд ниже,"
                      " прежде чем использовать меня, или начни прямо сейчас!",
        "see_more_but": "Подробнее..",
        "share": "Привет, я использую @GPTypeBot, это очень удобно!"
    }
}

facts = {
    "en": {
        "end_with_sign": {
            "title": "Remember query ends with '{}' / '{}' / '{}' / '{}'".format(
                DotSign.marker,
                ExclamationSign.marker,
                QuestionSign.marker,
                SimpleEndMarker.marker
            ),
            "description": "Please read documentation https://docs.google.com/document/d/"
                           "1hlicXB2bXyMTzR2qT5vUPJWUc4gEyIEIydRmepH7p0Y/edit?usp=drivesdk",
            "photo": "https://i.ibb.co/8KyTTdy/warning.png"
        },
        "wrong_marker_use": {
            "title": "Check correctness of marker {}",
            "description": "Please read documentation https://docs.google.com/document/d/"
                           "1hlicXB2bXyMTzR2qT5vUPJWUc4gEyIEIydRmepH7p0Y/edit?usp=drivesdk",
            "photo": "https://i.ibb.co/HN8RcKs/cancel.png"
        },
        "too_long_query": {
            "title": "Query is over 255 symbols. Telegram limit😢",
            "description": "Please read documentation https://docs.google.com/document/d/"
                           "1hlicXB2bXyMTzR2qT5vUPJWUc4gEyIEIydRmepH7p0Y/edit?usp=drivesdk",
            "photo": "https://i.ibb.co/HN8RcKs/cancel.png"
        }
    },
    "uk": {
        "end_with_sign": {
            "title": "Пам'ятай, запит закінчується на '{}' / '{}' / '{}' / '{}'".format(
                DotSign.marker,
                ExclamationSign.marker,
                QuestionSign.marker,
                SimpleEndMarker.marker
            ),
            "description": "Please read documentation https://docs.google.com/document/d/"
                           "1hlicXB2bXyMTzR2qT5vUPJWUc4gEyIEIydRmepH7p0Y/edit?usp=drivesdk",
            "photo": "https://i.ibb.co/8KyTTdy/warning.png"
        },
        "wrong_marker_use": {
            "title": "Перевір правильність маркеру {}",
            "description": "Please read documentation https://docs.google.com/document/d/"
                           "1hlicXB2bXyMTzR2qT5vUPJWUc4gEyIEIydRmepH7p0Y/edit?usp=drivesdk",
            "photo": "https://i.ibb.co/HN8RcKs/cancel.png"
        },
        "too_long_query": {
            "title": "Запит більше ніж 255 символів. Це ліміт Телеграму😢",
            "description": "Please read documentation https://docs.google.com/document/d/"
                           "1hlicXB2bXyMTzR2qT5vUPJWUc4gEyIEIydRmepH7p0Y/edit?usp=drivesdk",
            "photo": "https://i.ibb.co/HN8RcKs/cancel.png"
        }
    },
    "ru": {
        "end_with_sign": {
            "title": "Помни, запрос заканчивается на '{}' / '{}' / '{}' / '{}'".format(
                DotSign.marker,
                ExclamationSign.marker,
                QuestionSign.marker,
                SimpleEndMarker.marker
            ),
            "description": "Please read documentation https://docs.google.com/document/d/"
                           "1hlicXB2bXyMTzR2qT5vUPJWUc4gEyIEIydRmepH7p0Y/edit?usp=drivesdk",
            "photo": "https://i.ibb.co/8KyTTdy/warning.png"
        },
        "wrong_marker_use": {
            "title": "Проверь правильность маркера {}",
            "description": "Please read documentation https://docs.google.com/document/d/"
                           "1hlicXB2bXyMTzR2qT5vUPJWUc4gEyIEIydRmepH7p0Y/edit?usp=drivesdk",
            "photo": "https://i.ibb.co/HN8RcKs/cancel.png"
        },
        "too_long_query": {
            "title": "Запрос больше 255 символов. Это лимит Телеграма😢",
            "description": "Please read documentation https://docs.google.com/document/d/"
                           "1hlicXB2bXyMTzR2qT5vUPJWUc4gEyIEIydRmepH7p0Y/edit?usp=drivesdk",
            "photo": "https://i.ibb.co/HN8RcKs/cancel.png"
        }
    }
}
