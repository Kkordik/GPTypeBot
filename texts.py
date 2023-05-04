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
        "query_out_of_time": "☝🏻Get the result in pm",
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
        "query_out_of_time": "☝🏻Отримати результат в лс",
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
        "query_out_of_time": "☝🏻Получить результат в лс",
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
        "introduction": {
            "description": "<b>Introduction</b>\n\nThe OpenAI-powered @GPTypeBot bot is a powerful tool for generating"
                           " text quickly and easily. It can generate text for a wide range of purposes,"
                           " including writing formal letters, correcting mistakes, translating to different languages,"
                           " and writing social media posts. This manual will guide you through using"
                           " the bot's various functions and explain how to make a query using both the inline query"
                           " and private message query methods.",
            "button": "Introduction",
            "examples": []
        },
        "inline_method": {
            "description": "<b>Inline Method</b>\n\nInline Method is a way of sending a query to the bot directly from "
                           "any Telegram chat or group without the need to open a separate chat with the bot.\nTo start"
                           " the query, the user simply types in bot's username followed by a space and then the query"
                           " itself.\nThe bot will then process the query and return the result in the same chat where "
                           "the query was made.\nThis method is useful when you want to get and send result fastly.",
            "button": "Inline Bots",
            "examples": []
        },
        "query_methods": {
            "description": "<b>Private Message Method:</b>"
                           "\nTo make a query using the private message method, send your query directly to "
                           "the bot in a private message.\nThis method is useful when you want to keep your queries"
                           " private.",
            "button": "Query Methods",
            "examples": []
        },
        "query_syntax": {
            "description": "<b>Query Syntax:</b>\n\n<b>Both the Inline and Private Messages methods have the same"
                           " query syntax with one difference:\n• The query in the Inline method always starts with"
                           " the bot's username @GPTypeBot and a space: '@GPTypeBot '\n• However, in the Private"
                           " Messages method, the query should never start with the bot's username.</b>",
            "button": "Queries Syntax",
            "examples": []
        },
        "query_syntax2": {
            "description": "<b>1. The query always consists of <u>sub-query blocks</u> and <u>static texts</u>:"
                           "\n    1.1. Static text is text that won't be passed into the OpenAI GPT Model and will be "
                           "returned at the same position as it was given."
                           "\n    1.2. A sub-query block is a question or request that will be passed to the GPT Model."
                           " Its text is always between <u>start marker</u> "
                           "and <u>finish marker</u> (but if there is only one block, markers can be omitted).</b>",
            "button": "Syntax 2",
            "examples": []
        },
        "examples": {
            "description": "In the examples below, '-s' is used as the start marker and '-q' as the finish marker. "
                           "These are the simplest markers and mean the start of a sub-query and its finish. "
                           "More complex markers will be explained later.\n\nExamples:\n\n<b>Single sub-query:</b>\n"
                           "'@GPTypeBot <code>-s How to cook borshch? -q</code>'\n"
                           "Here is only one sub-query block without static text, so all markers can be omitted:\n"
                           "'@GPTypeBot <code>How to cook borshch ?</code>'\n<i>Notice, if query doesn't end with"
                           " finish marker, it must end with one of the punctuation signs (./!/?)</i>\n\n"
                           "<b>Sub-query with static text after:</b>\n"
                           "'@GPTypeBot <code>-s How to cook borshch? -q My grandma's recipe .</code>'\n"
                           "<i>Don't forget about punctuation sign</i>\n\n"
                           "<b>Sub-query with static text before:</b>\n"
                           "'@GPTypeBot <code>My grandma's recipe: -s How to cook borshch ?</code>'"
                           "<i>Here static text is before the sub-query block.</i>\n\n"
                           "<b>Two sub-queries with static texts everywhere:</b>\n"
                           "'@GPTypeBot <code>My grandma's recipe: -s How to cook borshch? -q I used to eat it every"
                           " day! -s Is borshch healthy? -q It can explain why I visit doctor so rarely .</code>'"
                           "\nAs you can see, this query has two sub-queries because their amount is not limited.\n"
                           "Notice, static text is not required and can be omitted:\n"
                           " '@GPTypeBot <code>-s How to cook borshch? -q -s Is borshch healthy ?</code>'\n\n"
                           "You can try inline examples, clicking on the buttons below or"
                           " you can try private message examples copying (just click on its text) "
                           "and sending queries to the chat with bot",
            "button": "Syntax Examples",
            "examples": [{"button": "Single sub-query", "query": "How to cook borshch ?"},
                         {"button": "Static text after", "query": "-s How to cook borshch? -q My grandma's recipe ."},
                         {"button": "Static text before:", "query": "My grandma's recipe: -s How to cook borshch ?"},
                         {"button": "Two sub-queries, static texts", "query": "My grandma's recipe: -s How to cook "
                                                                              "borshch? -q I used to eat it every day! "
                                                                              "-s Is borshch healthy? -q It can explain"
                                                                              " why I visit doctor so rarely ."},
                         {"button": "Two sub-queries", "query": "-s How to cook borshch? -q -s Is borshch healthy ?"}]
        },
        "markers_list": {
            "description": "<b>Markers</b>\n\nMarkers are used to separate sub-queries and to specify its "
                           "handling type.\n\n<b>Begin Markers:</b>\n"
                           "<b>'<code>-s</code>'</b>   is a simple start marker. Doesn't have any specific handling.\n"
                           "<b>'<code>-f</code>'</b>   is a formal start marker. Writes a formal message based on the given theme.\n"
                           "<b>'<code>-p</code>'</b>   is a post start marker. Creates a post based on the given theme and details.\n"
                           "<b>'<code>-t-language</code>'</b>   is a translate start marker. Translates given text to the specified"
                           " language\n"
                           "<b>'<code>-m</code>'</b>   is a mistakes start marker. Corrects mistakes in the given text.\n\n"
                           "<b>End Marker:</b>\n"
                           "<b>'<code>-q</code>'</b>   is a quit end marker. Is used to finish queries and sub-queries.",
            "button": "Markers",
            "examples": [
                {"button": "Example -f", "query": "-f Alex, I am late, sorry, traffic jams!"},
                {"button": "Example -p", "query": "-p We have to stop climate changing or it will kill us!"},
                {"button": "Example -t", "query": "-t-spanish Hi! My name is Max, glad to see you in this chat!"},
                {"button": "Example -m", "query": "-m I have jast told u thet I will continu sleping!"},
                {"button": "Example -q", "query": "-s Give me 5 reasons why should I start exercising -q"},
            ]
        }
    },
    "uk": {
        "inline_bot": {
            "description": "Це вбудований(inline) бот, а це значить, що ви можете використовувати його в будь-якому чаті,"
                           " без необхідності додавати в групу. "
                           "\nЩоб звернутися до боту - введіть @GPTypeBot у полі введення тексту",
            "button": "Вбудований бот",
            "examples": []
        },
        "simple_query": {
            "description": "Після звернення до боту, введіть свій запит, він може бути простим або з маркерами\n\n"
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
            "description": "Это встроенный(inline) бот, то есть вы можете использовать его в любом чате, "
                           "без необходимости добавления в группу. \nЧтобы обратиться к боту - введите @GPTypeBot в поле ввода текста",
            "button": "Встроенный бот",
            "examples": []
        },
        "simple_query": {
            "description": "После обращения к боту, введите свой запрос, который может быть простым или с маркерами\n\n"
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
                example: dict
                example_queries.append(example["query"])
