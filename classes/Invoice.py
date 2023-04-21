import time

import aiogram
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiocryptopay import AioCryptoPay, Networks
from aiocryptopay.models.invoice import Invoice
from config import CRYPTOBOT_TOKEN, CURRENCIES_API_KEY, WAYFORPAY_TOKEN, LIQ_PAY_TOKEN
from texts import texts
import hashlib
import hmac
import aiohttp


class MyInvoice:
    button_name: str
    method_name: str
    _currencies_list: list
    default_currency: str
    invoice_text_name: str
    need_status_check_loop: bool

    def __init__(self, amount: float = None, currency: str = None, product_name: str = None, client_user_id=None, client_name: str = None,
                 invoice_parameter: str = None, invoice_status: bool = None):
        self.invoice_time: int = int(time.time())
        self.client_user_id = client_user_id
        self.client_name = client_name
        self.currency = currency
        self.product_name = product_name
        self.amount = amount
        self.invoice_parameter: str = invoice_parameter
        self.invoice_status: bool = invoice_status

    @staticmethod
    def find_create_invoice_object(pay_method_name: str):
        for sub_my_invoice_cl in MyInvoice.__subclasses__():
            sub_my_invoice_cl = sub_my_invoice_cl()
            if pay_method_name == sub_my_invoice_cl.method_name:
                return sub_my_invoice_cl
        return None

    @staticmethod
    def payment_url_keyboard(lang: str, pay_url: str, payment_method: str, parameter: str) -> InlineKeyboardMarkup:
        return InlineKeyboardMarkup()

    def calculate_price(self, chosen_currency, usd_price):
        pass

    async def create_invoice_url(self, bot: aiogram.Bot):
        pass

    async def check_invoice(self, invoice_parameter: str = None):
        pass

    async def get_currencies_list(self):
        return self._currencies_list

    def get_callback_data(self):
        return "payment_method-" + self.method_name

    async def get_currency_callback_data(self, chosen_currency):
        return "payment_currency-" + self.method_name + "-" + chosen_currency

    def get_invoice_parameter(self) -> str:
        pass


class CryptoInvoice(MyInvoice):
    button_name = "crypto_method_but"
    method_name = "crypto"
    _currencies_list = ["BTC", "TON", "ETH", "USDT", "USDC", "BUSD"]
    default_currency = "USDT"
    invoice_text_name = "crypto_invoice"
    need_status_check_loop = True

    __price_url = "https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest"
    __crypto = AioCryptoPay(token=CRYPTOBOT_TOKEN, network=Networks.TEST_NET)  # Change MAIN_NET on TEST_NET to test bot

    def __init__(self, amount: float = None, currency: str = None, client_user_id=None, client_name: str = None,
                 invoice: Invoice = None, invoice_status: bool = None, invoice_parameter: str = None):
        super().__init__(amount, currency, client_user_id, client_name, invoice_parameter, invoice_status)
        self.invoice: Invoice = invoice

    @staticmethod
    def payment_url_keyboard(lang: str, pay_url: str, payment_method: str, parameter: str):
        keyboard = InlineKeyboardMarkup()
        if pay_url:
            keyboard.add(InlineKeyboardButton(text=texts[lang]["pay_but"], url=pay_url))
            keyboard.add(InlineKeyboardButton(text=texts[lang]["paid_but"],
                                              callback_data=f"check_payment-{payment_method}-{parameter}"))
        return keyboard

    async def get_currencies_list(self):
        currencies_list = await self.__crypto.get_currencies()
        self._currencies_list = []
        for currency in currencies_list:
            if not currency.is_fiat:
                self._currencies_list.append(currency.code)
        return self._currencies_list

    async def calculate_price(self, chosen_currency, usd_price):
        parameters = {'symbol': chosen_currency,
                      'convert': 'USD'}
        headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': CURRENCIES_API_KEY
        }

        session = aiohttp.ClientSession()
        session.headers.update(headers)
        response = await session.get(self.__price_url, params=parameters)
        response = await response.json()
        currency_price = response['data'][chosen_currency][0]['quote']['USD']['price']

        return usd_price / currency_price

    async def create_invoice_url(self, bot: aiogram.Bot) -> str:
        self.invoice = await self.__crypto.create_invoice(asset=self.currency, amount=self.amount)
        self.invoice_parameter = str(self.invoice.invoice_id)
        return self.invoice.pay_url

    async def check_invoice(self, invoice_parameter: str = None) -> bool:
        if invoice_parameter:
            self.invoice_parameter = invoice_parameter
        elif self.invoice_parameter:
            pass
        elif self.invoice:
            self.invoice_parameter = str(self.invoice.invoice_id)
        else:
            raise Exception("No self.invoice or self.invoice_parameter specified to check status")

        gotten_invoice = await self.__crypto.get_invoices(invoice_ids=int(self.invoice_parameter))

        self.invoice_status = True if gotten_invoice.status == gotten_invoice.status.PAID else False

        return self.invoice_status

    def get_invoice_parameter(self) -> str:
        if not self.invoice:
            raise Exception("No self.invoice specified before, cant create invoice_parameter")

        invoice_id = str(self.invoice.invoice_id)
        self.invoice_parameter = hashlib.md5(invoice_id.encode()).hexdigest()
        return self.invoice_parameter


class CardInvoice(MyInvoice):
    button_name = "card_method_but"
    method_name = "card"
    _currencies_list = ["UAH"]
    default_currency = "UAH"
    invoice_text_name = "card_invoice"
    need_status_check_loop = False


    __WFP_TOKEN = WAYFORPAY_TOKEN
    __merchant_name = "t_me_4381e"
    __merchant_domain = "http://t.me/GPTypeBot"
    __wfp_url = "https://api.wayforpay.com/api"
    __wfp_session = aiohttp.ClientSession()

    def __init__(self, amount: float = None, currency: str = None, client_user_id=None, client_name: str = None,
                 invoice_parameter: str = None, invoice_status: bool = None):
        super().__init__(amount, currency, client_user_id, client_name, invoice_parameter, invoice_status)

    def get_invoice_parameter(self) -> str:
        if not self.client_user_id:
            raise Exception("No self.client_user_id specified before, cant create invoice_parameter")

        if not self.invoice_parameter:
            param_to_hash = str(self.client_user_id) + str(self.invoice_time)
            self.invoice_parameter = hashlib.md5(param_to_hash.encode()).hexdigest()
        return self.invoice_parameter

    def __generate_message_hash(self, message_vals: list = None, sep: str = ';') -> str:
        message = sep.join([str(obj) for obj in message_vals])
        print(message)
        print(self.__WFP_TOKEN)
        msg_hmac = hmac.new(key=self.__WFP_TOKEN.encode('utf-8'),
                            msg=message.encode('utf-8'),
                            digestmod='MD5')
        return msg_hmac.hexdigest()

    async def calculate_price(self, chosen_currency, usd_price):
        msg_hash = self.__generate_message_hash([self.__merchant_name, self.invoice_time])
        data = {
            "apiVersion": "1",
            "transactionType": "CURRENCY_RATES",
            "merchantAccount": self.__merchant_name,
            "orderDate": self.invoice_time,
            "merchantSignature": msg_hash
        }
        print(data)
        response = await self.__wfp_session.post(self.__wfp_url, json=data)
        response = await response.json(content_type='text/html')

        return usd_price * int(response['rates']['USD'])

    async def create_invoice_url(self, bot: aiogram.Bot) -> str:
        url = await bot.create_invoice_link(
            title='GPTypeBot subscription',
            description='Become premium user of t.me/GPTypeBot',
            payload=self.invoice_parameter,
            provider_token=LIQ_PAY_TOKEN,
            currency='UAH',
            prices=[aiogram.types.LabeledPrice(label='premium', amount=int(self.amount) * 100)]
        )
        return url
