from classes.Markers import DotSign, ExclamationSign, QuestionSign, SimpleEndMarker

texts = {
    "en": {
        "start_text": "Hello! its gptype bot",
        "see_more_but": "See more"
    },
    "uk": {
        "start_text": "Привіт! це чат гпт",
        "see_more_but": "See more"
    },
    "ru": {
        "start_text": "Привет! это чат гпт",
        "see_more_but": "See more"
    }
}

facts = {
    "en": {
        "end_with_sign": "End query with one of '{}'  '{}'  '{}'  '{}'".format(DotSign.marker,
                                                                               ExclamationSign.marker,
                                                                               QuestionSign.marker,
                                                                               SimpleEndMarker.marker),
        "wrong_marker_use": "Check correctness of markers {}",
        "too_long_query": "Query is over 255 symbols. Telegram limit"
    },
    "uk": {
        "end_with_sign": "Uk End query with one of '{}'  '{}'  '{}'  '{}'".format(DotSign.marker,
                                                                                  ExclamationSign.marker,
                                                                                  QuestionSign.marker,
                                                                                  SimpleEndMarker.marker),
        "wrong_marker_use": "Uk Check correctness of markers {}",
        "too_long_query": "Uk Query is over 255 symbols. Telegram limit"
    },
    "ru": {
        "end_with_sign": "Ru End query with one of '{}'  '{}'  '{}'  '{}'".format(DotSign.marker,
                                                                                  ExclamationSign.marker,
                                                                                  QuestionSign.marker,
                                                                                  SimpleEndMarker.marker),
        "wrong_marker_use": "Ru Check correctness of markers {}",
        "too_long_query": "Ru Query is over 255 symbols. Telegram limit"
    }
}

facts_desc = {
    "en": {
        "end_with_sign": "Please read documentation https://docs.google.com/document/d/"
                         "1hlicXB2bXyMTzR2qT5vUPJWUc4gEyIEIydRmepH7p0Y/edit?usp=drivesdk",
        "wrong_marker_use": "Please read documentation https://docs.google.com/document/d/"
                            "1hlicXB2bXyMTzR2qT5vUPJWUc4gEyIEIydRmepH7p0Y/edit?usp=drivesdk",
        "too_long_query": "Unfortunately telegram has limit in 255 symbols in inline query😢 "
                          "It is impossible to do something with it"
    },
    "uk": {
        "end_with_sign": "Uk Please read documentation https://docs.google.com/document/d/"
                         "1hlicXB2bXyMTzR2qT5vUPJWUc4gEyIEIydRmepH7p0Y/edit?usp=drivesdk",
        "wrong_marker_use": "Uk Please read documentation https://docs.google.com/document/d/"
                            "1hlicXB2bXyMTzR2qT5vUPJWUc4gEyIEIydRmepH7p0Y/edit?usp=drivesdk",
        "too_long_query": "Uk Unfortunately telegram has limit in 255 symbols in inline query😢 "
                          "It is impossible to do something with it"

    },
    "ru": {
        "end_with_sign": "Ru Please read documentation https://docs.google.com/document/d/"
                         "1hlicXB2bXyMTzR2qT5vUPJWUc4gEyIEIydRmepH7p0Y/edit?usp=drivesdk",
        "wrong_marker_use": "Ru Please read documentation https://docs.google.com/document/d/"
                            "1hlicXB2bXyMTzR2qT5vUPJWUc4gEyIEIydRmepH7p0Y/edit?usp=drivesdk",
        "too_long_query": "Ru Unfortunately telegram has limit in 255 symbols in inline query😢 "
                          "It is impossible to do something with it"
    }
}
