from classes.Markers import BeginMarker, DotSign, ExclamationSign, QuestionSign, SimpleEndMarker
from config import TELEGRAM_CHAR_LIMIT, SUBSCRIPTION_PRICE

texts = {
    "en": {
        "oferta_msg": "Користувацька угода\n\nФОП Буткевич А.И.\n+380939530473\nАдмін +380502330052",
        "start_text": "Powerful, unique and easy.\nCheck the short guide below before using me or start right now!"
                      "\n\nYou have {} trial inline queries\n\nFeedback: @kkordik",
        "start_text_subs": "Powerful, unique and easy.\nCheck the short guide below before using me or start "
                           "right now!\n\nFeedback: @kkordik",
        "see_more_but": "See more..",
        "buy_subs_but": "Buy now..",
        "get_in_pm_but": "Send in pm with bot",
        "premium_but": "👑 Premium",
        "share": "Hello I use @GPTypeBot, it is very convenient!",
        "guide_but": "📖 Guide",
        "start_inline_use_but": "🟢 Start using",
        "getting_query_ready": "Processing your request ♻️",
        "context_but": "⚙️ Context",
        "waiting_for_openai": "Waiting for OpenAI answer ⏳",
        "topics_msg": "Your topics, click to choose which topic you want to use:",
        "create_topic_but": "➕ Create new",
        "no_topic": "⚡️ No context",
        "topics_not_subs": "Oops, looks like you don't have a subscription, context is available only for premium "
                           "subscribers, see more such features and become a subscriber by button below:",
        "send_topic_title": "Send title for a new topic",
        "already_chosen": "⛔️ It is already chosen",
        "cancel_but": "❌ Cancel",
        "canceled": "☑️ Canceled",
        "topic_but_chosen": "📌 '{}' ({} requests)",
        "topic_but": "'{}' ({} msgs)",
        "return_inline_but": "Return to the chat",
        "return_approve_but": "Confirm returning",
        "already_premium": "You are already premium subscriber❤️",
        "premium_benefits": "What month premium subcription gives, click to see more:"
                            "\n\n-Inline queries in any chat"
                            "\n-Unlimited amount of queries"
                            "\n-History of queries"
                            f"\n\nPrice {SUBSCRIPTION_PRICE} dollars/month"
                            "\n\nChoose payment method:",
        "crypto_method_but": "🌑 Crypto",
        "card_method_but": "💳 Visa | Mastercard",
        "back_payment_but": "Return",
        "crypto_invoice": "Pay by the button below, your subscription will be added automatically within 5 min:",
        "card_invoice": "Pay by the button below, your subscription will be added automatically after payment\n\nUser agreement: /oferta",
        "pay_but": "➡️Pay",
        "paid_but": "✅ I've paid",
        "successfully_paid": "Thank you for subscribing❤️, enjoy the full functionality of the bot, exactly in 28 days you will receive an invoice for a new payment, and after 30 in case of non-payment, the subscription will end",
        "not_paid": "❌ Not paid",
        "subs_pay_title": "GPTypeBot subscription",
        "subs_pay_description": "Become a t.me/GPTypeBot premium user",
        "subs_pay_label": "Premium subscription"
    },
    "uk": {
        "oferta_msg": "Користувацька угода\n\nФОП Буткевич А.И.\n+380939530473\nАдмін +380502330052",
        "start_text": "Могутній, унікальний та легкий.\nПереглянь короткий гайд нижче,"
                      " перш ніж користуватися мною, або почни прямо зараз!\n\nУ тебе є {} пробних інлайн запитів\n\nFeedback: @kkordik",
        "start_text_subs": "Могутній, унікальний та легкий.\nПереглянь короткий гайд нижче,"
                      " перш ніж користуватися мною, або почни прямо зараз!\n\nFeedback: @kkordik",
        "see_more_but": "Подробиці..",
        "buy_subs_but": "Придбати..",
        "get_in_pm_but": "Надіслати в лс з ботом",
        "premium_but": "👑 Преміум",
        "share": "Привіт, я використовую @GPTypeBot, це дуже зручно!",
        "guide_but": "📖 Гайд",
        "start_inline_use_but": "🟢 Почати використовувати",
        "getting_query_ready": "Опрацювання запиту ♻️",
        "context_but": "⚙️ Контекст",
        "waiting_for_openai": "Очікування відповіді від OpenAI ⏳",
        "topics_msg": "Твої теми, натисни щоб ту, яку хочеш використовувати:",
        "create_topic_but": "➕ Створити нову",
        "no_topic": "⚡️ Без контексту",
        "topics_not_subs": "Упс, схоже що у вас немає підписки, контекст доступний тільки для преміум підписників, "
                           "більше таких фішок та підписка за кнопкою:",
        "send_topic_title": "Надійшли назву для нової теми:",
        "already_chosen": "⛔️ Це вже обрано",
        "cancel_but": "❌ Скасувати",
        "canceled": "☑️ Скасовано",
        "topic_but_chosen": "📌 '{}' ({} смс)",
        "topic_but": "'{}' ({} смс)",
        "return_inline_but": "Повернутись до чату",
        "return_approve_but": "Підтвердити повернення",
        "already_premium": "Ти вже преміум підписник❤️",
        "premium_benefits": "Що дає місячна преміум підписка, клацай щоб подивитись детальніше:"
                            "\n\n-Інлайн запити в любих чатах"
                            "\n-Безліміт кількості запитів"
                            "\n-Пам'ять історії запитів"
                            f"\n\nЦіна {SUBSCRIPTION_PRICE} доларів/міс"
                            "\n\nОбери спосіб оплати:",
        "crypto_method_but": "🌑 Криптовалюта",
        "card_method_but": "💳 Visa | Mastercard",
        "back_payment_but": "Назад",
        "crypto_invoice": "Щоб сплатити перейди по кнопці нижче, твоя підписка обновиться автоматично на протязі 5хв:",
        "card_invoice": "Щоб сплатити перейди по кнопці нижче, твоя підписка обновиться автоматично після оплати\n\nКористувацька угода: /oferta",
        "pay_but": "➡️Оплатить",
        "paid_but": "✅ Я сплатив",
        "successfully_paid": "Дякуємо за підписку❤️, насолоджуйтесь повним функціоналом бота, рівно через 28 днів ви отримаєте рахунок на новий платіж, а через 30 у разі несплати підписка завершується",
        "not_paid": "❌ Не сплачено",
        "subs_pay_title": "GPTypeBot підписка",
        "subs_pay_description": "Стань t.me/GPTypeBot преміум юзером",
        "subs_pay_label": "Преміум підписка",
        "admin_successful_pay": "Новий платіж #{},\n\nОтримано {} {} від \n\nusername: @{} \nім'я: {} \nuser_id: {}"
    },
    "ru": {
        "oferta_msg": "Користувацька угода\n\nФОП Буткевич А.И.\n+380939530473\nАдмін +380502330052",
        "start_text": "Мощный, уникальный и лёгкий.\nПроверь краткий гайд ниже,"
                      " прежде чем использовать меня, или начни прямо сейчас!\n\nУ тебя есть {} пробных инлайн запросов\n\nFeedback: @kkordik",
        "start_text_subs": "Мощный, уникальный и лёгкий.\nПроверь краткий гайд ниже,"
                      " прежде чем использовать меня, или начни прямо сейчас!\n\nFeedback: @kkordik",
        "see_more_but": "Подробнее..",
        "buy_subs_but": "Купить..",
        "get_in_pm_but": "Прислать в лс с ботом",
        "premium_but": "👑 Премиум",
        "share": "Привет, я использую @GPTypeBot, это очень удобно!",
        "guide_but": "📖 Гайд",
        "start_inline_use_but": "🟢 Начать использовать",
        "getting_query_ready": "Обработка запроса ♻️",
        "context_but": "⚙️ Контекст",
        "waiting_for_openai": "Ожидание ответа OpenAI ⏳",
        "topics_msg": "Твои темы, нажми чтобы выбрать ту, которую хочешь использовать:",
        "create_topic_but": "➕ Создать новую",
        "no_topic": "⚡️ Без контекста",
        "topics_not_subs": "Упс, походе что у вас нету подписки, контекст доступный только для премиум родписчиков, "
                           "больше таких фишек и подписка по кнопке:",
        "send_topic_title": "Пришли название для новой темы:",
        "already_chosen": "⛔️ Это уже выбрано",
        "cancel_but": "❌ Отменить",
        "canceled": "☑️ Отменено",
        "topic_but_chosen": "📌 '{}' ({} смс)",
        "topic_but": "'{}' ({} смс)",
        "return_inline_but": "Вернуться в чат",
        "return_approve_but": "Подтвердить возвращение",
        "already_premium": "У тебя уже есть премиум подписка❤️",
        "premium_benefits": "Что даёт месячная премиум подписка, клацай чтобы посмотреть подробнее:"
                            "\n\n-Инлайн запросы в любых чатах"
                            "\n-Безлимит количества запросов"
                            "\n-Память истории запросов"
                            f"\n\nЦена {SUBSCRIPTION_PRICE} долларов/мес"
                            "\n\nВыбери способ оплаты:",
        "crypto_method_but": "🌑 Криптовалюта",
        "card_method_but": "💳 Visa | Mastercard",
        "back_payment_but": "Назад",
        "crypto_invoice": "Чтобы оплатить перейди по кнопке ниже, твоя подписка обновиться автоматически в течении 5 мин:",
        "card_invoice": "Чтобы оплатить перейди по кнопке ниже, твоя подписка обновиться автоматически после оплаты\n\nПользовательское соглашение: /oferta",
        "pay_but": "➡️Оплатить",
        "paid_but": "✅ Я оплатил",
        "successfully_paid": "Спасибо за подписку❤️, наслаждайтесь полным функционалом бота, ровно через 28 дней вам придёт счет на новую оплату, а через 30 в случае неоплаты подписка закончится",
        "not_paid": "❌ Не оплачено",
        "subs_pay_title": "GPTypeBot подписка",
        "subs_pay_description": "Стань t.me/GPTypeBot премиум юзером",
        "subs_pay_label": "Пермиум подписка"
    }
}

facts = {
    "en": {
        "start_with_marker":  "Ask or use marker ({})".format(
            " / ".join([b_marker.marker for b_marker in BeginMarker.__subclasses__()])
        ),

        "end_with_sign":  "To end use ({} / {} / {} / {})".format(
                           DotSign.marker,
                           ExclamationSign.marker,
                           QuestionSign.marker,
                           SimpleEndMarker.marker
        ),
        "wrong_marker_use": "Looks like '{}' is wrongly used",
        "too_long_query": f"Query is over {TELEGRAM_CHAR_LIMIT} symbols. Telegram limit😢",
        "waiting_time": "10s is average answering time",
        "no_subscription": "Only for premium subscribers",
        "unknown_error": "Sorry, try again later",
        "ask_later": "Wait {}s to ask new query",
        "current_topic": "Current topic: '{}'"
    },
    "uk": {
        "start_with_marker":  "Запитуй або пиши маркер ({})".format(
            " / ".join([b_marker.marker for b_marker in BeginMarker.__subclasses__()])
        ),
        "end_with_sign": "Закінчуй маркером ({} / {} / {} / {})".format(
                          DotSign.marker,
                          ExclamationSign.marker,
                          QuestionSign.marker,
                          SimpleEndMarker.marker
        ),
        "wrong_marker_use": "Схоже, що '{}' неправильно використано",
        "too_long_query": f"Запит більше ніж {TELEGRAM_CHAR_LIMIT} символів. Це ліміт Телеграму😢",
        "waiting_time": "10 сек. це середній час відповіді",
        "no_subscription": "Тільки для преміум підписників",
        "unknown_error": "Вибач, спробуй ще раз пізніше",
        "ask_later": "Почекай ще {} сек для можливості нового запиту",
        "current_topic": "Обрана тема: '{}'"
    },
    "ru": {
        "start_with_marker": "Спрашивай или юзай маркер ({})".format(
            " / ".join([b_marker.marker for b_marker in BeginMarker.__subclasses__()])
        ),

        "end_with_sign": "Заканчивай маркером ({} / {} / {} / {})".format(
                          DotSign.marker,
                          ExclamationSign.marker,
                          QuestionSign.marker,
                          SimpleEndMarker.marker
        ),
        "wrong_marker_use": "Похоже, что '{}' неправильно использовано",
        "too_long_query": f"Запрос больше {TELEGRAM_CHAR_LIMIT} символов. Это лимит Телеграма😢",
        "waiting_time": "10 сек. это среднее время ответа",
        "no_subscription": "Только для премиум подписчиков",
        "unknown_error": "Извини, попробуй еще раз позже",
        "ask_later": "Подожди ещё {} сек для нового запроса",
        "current_topic": "Используемая тема: '{}'"
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

example_queries = []

# Add all example queries to the list
for lang in guide_texts.values():
    for text_dict in lang.values():
        if text_dict["examples"]:
            for example in text_dict["examples"]:
                example_queries.append(example["query"])
