from aiocryptopay import AioCryptoPay, Networks
from aiocryptopay.models.invoice import Invoice
from config import CRYPTOBOT_TOKEN, CURRENCIES_API_KEY, SUBSCRIPTION_PRICE
from requests import Session
import json


class MyInvoice:
    button_name: str
    method_name: str
    _currencies_list: list
    default_currency: str
    invoice_text_name: str
    invoice_parameter: str

    def __init__(self, amount: float = None, currency: str = None):
        self.currency = currency
        self.amount = amount

    @staticmethod
    def find_create_invoice_object(pay_method_name: str):
        for sub_my_invoice_cl in MyInvoice.__subclasses__():
            sub_my_invoice_cl = sub_my_invoice_cl()
            if pay_method_name == sub_my_invoice_cl.method_name:
                return sub_my_invoice_cl
        return None

    def calculate_price(self, chosen_currency):
        pass

    async def create_invoice_url(self):
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
    price_url = "https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest"
    button_name = "crypto_method_but"
    method_name = "crypto"
    _currencies_list = ["BTC", "TON", "ETH", "USDT", "USDC", "BUSD"]
    default_currency = "USDT"
    crypto = AioCryptoPay(token=CRYPTOBOT_TOKEN, network=Networks.MAIN_NET)  # Change from MAIN_NET on TEST_NET to test
    invoice_text_name = "crypto_invoice"

    def __init__(self, amount: float = None, currency: str = None, invoice: Invoice = None, invoice_status: bool = None):
        super().__init__(amount, currency)
        self.invoice: Invoice = invoice
        self.invoice_status: bool = invoice_status

    async def get_currencies_list(self):
        currencies_list = await self.crypto.get_currencies()
        self._currencies_list = []
        for currency in currencies_list:
            if not currency.is_fiat:
                self._currencies_list.append(currency.code)
        return self._currencies_list

    def calculate_price(self, chosen_currency):
        parameters = {'symbol': chosen_currency,
                      'convert': 'USD'}
        headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': CURRENCIES_API_KEY
        }

        session = Session()
        session.headers.update(headers)

        response = session.get(self.price_url, params=parameters)

        currency_price = json.loads(response.text)['data'][chosen_currency][0]['quote']['USD']['price']

        return SUBSCRIPTION_PRICE / currency_price

    async def create_invoice_url(self) -> str:
        self.invoice = await self.crypto.create_invoice(asset=self.currency, amount=self.amount)
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
            raise Exception("No invoice or invoice parameter specified to check status")

        gotten_invoice = await self.crypto.get_invoices(invoice_ids=int(self.invoice_parameter))

        self.invoice_status = True if gotten_invoice.status == gotten_invoice.status.PAID else False

        return self.invoice_status

    def get_invoice_parameter(self) -> str:
        return str(self.invoice.invoice_id)


class CardInvoice(MyInvoice):
    button_name = "card_method_but"
    method_name = "card"
    _currencies_list = ["UAH"]
    default_currency = "UAH"
    invoice_text_name = "card_invoice"

    def __init__(self):
        super().__init__()

