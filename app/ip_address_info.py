import requests

from app.core.config import settings
from app.schemas import IPinfo


class IPAddress:
    def __init__(self, ip_address):
        self.ip_address = ip_address

    def __get_country_info(self):
        country_info = requests.get(
            url=f'{settings.IP_GEOLOCATION_URL}/{self.ip_address}',
            params={'fields': 'country,countryCode,city,currency'}
        )

        response = country_info.json()

        self.country = response['country']
        self.country_code = response['countryCode']
        self.city = response['city']
        self.currency = response['currency']

    def __get_currency_info(self):
        currency_conversion = requests.get(
            url=f'{settings.CURRENCY_CONVERTER_URL}?base={self.currency}&symbols=EUR,USD',
            headers={'apikey': settings.CURRENCY_CONVERTER_APIKEY}
        )

        response = currency_conversion.json()

        self.to_eur = response['rates']['EUR']
        self.to_usd = response['rates']['USD']

    def __create_ip_info_schema(self):
        ip_info = IPinfo(
            country=self.country,
            country_code=self.country_code,
            city=self.city,
            currency=self.currency,
            currency_to_eur=self.to_eur,
            currency_to_usd=self.to_usd
        )

        return ip_info

    def get_info(self):
        self.__get_country_info()
        self.__get_currency_info()
        ip_info_schema = self.__create_ip_info_schema()
        return ip_info_schema
