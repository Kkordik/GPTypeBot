from classes.Markers import DotSign, ExclamationSign, QuestionSign, SimpleEndMarker

texts = {
    "en": {
        "start_text": "Hello! its gptype bot",
        "see_more_but": "See more",
        "share": "Hello I use @GPTypeBot, it is very convenient!"
    },
    "uk": {
        "start_text": "Привіт! це чат гпт",
        "see_more_but": "See more",
        "share": "Uk Hello I use @GPTypeBot, it is very convenient!"
    },
    "ru": {
        "start_text": "Привет! это чат гпт",
        "see_more_but": "See more",
        "share": "Ru Hello I use @GPTypeBot, it is very convenient!"
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
            "title": "Check correctness of markers {}",
            "description": "Please read documentation https://docs.google.com/document/d/"
                           "1hlicXB2bXyMTzR2qT5vUPJWUc4gEyIEIydRmepH7p0Y/edit?usp=drivesdk",
            "photo": "https://i.ibb.co/HN8RcKs/cancel.png"
        },
        "too_long_query": {
            "title": "Query is over 255 symbols. Telegram limit",
            "description": "Please read documentation https://docs.google.com/document/d/"
                           "1hlicXB2bXyMTzR2qT5vUPJWUc4gEyIEIydRmepH7p0Y/edit?usp=drivesdk",
            "photo": "https://i.ibb.co/HN8RcKs/cancel.png"
        }
    },
    "uk": {
        "end_with_sign": {
            "title": "Uk Remember query ends with '{}' / '{}' / '{}' / '{}'".format(
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
            "title": "Uk Check correctness of markers {}",
            "description": "Please read documentation https://docs.google.com/document/d/"
                           "1hlicXB2bXyMTzR2qT5vUPJWUc4gEyIEIydRmepH7p0Y/edit?usp=drivesdk",
            "photo": "https://i.ibb.co/HN8RcKs/cancel.png"
        },
        "too_long_query": {
            "title": "Uk Query is over 255 symbols. Telegram limit",
            "description": "Please read documentation https://docs.google.com/document/d/"
                           "1hlicXB2bXyMTzR2qT5vUPJWUc4gEyIEIydRmepH7p0Y/edit?usp=drivesdk",
            "photo": "https://i.ibb.co/HN8RcKs/cancel.png"
        }
    },
    "ru": {
        "end_with_sign": {
            "title": "Ru Remember query ends with '{}' / '{}' / '{}' / '{}'".format(
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
            "title": "Ru Check correctness of markers {}",
            "description": "Please read documentation https://docs.google.com/document/d/"
                           "1hlicXB2bXyMTzR2qT5vUPJWUc4gEyIEIydRmepH7p0Y/edit?usp=drivesdk",
            "photo": "https://i.ibb.co/HN8RcKs/cancel.png"
        },
        "too_long_query": {
            "title": "Ru Query is over 255 symbols. Telegram limit",
            "description": "Please read documentation https://docs.google.com/document/d/"
                           "1hlicXB2bXyMTzR2qT5vUPJWUc4gEyIEIydRmepH7p0Y/edit?usp=drivesdk",
            "photo": "https://i.ibb.co/HN8RcKs/cancel.png"
        }
    }
}
