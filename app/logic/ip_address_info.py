import requests
from fastapi import HTTPException, status

from app.core.config import settings
from app.schemas import IPinfo


class IPAddress:
    def __init__(self, ip_address):
        self.ip_address = ip_address

    def __get_country_info(self):
        country_info_request = requests.get(
            url=f'{settings.IP_GEOLOCATION_URL}/{self.ip_address}',
            params={'fields': 'status,message,country,countryCode,city,currency'}
        )

        country_info_response = country_info_request.json()

        if country_info_response['status'] == 'fail':
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail=country_info_response['message']
            )

        self.country = country_info_response['country']
        self.country_code = country_info_response['countryCode']
        self.city = country_info_response['city']
        self.currency = country_info_response['currency']

    def __get_currency_info(self):
        currency_conversion_request = requests.get(
            url=f'{settings.CURRENCY_CONVERTER_URL}?base={self.currency}&symbols=EUR,USD',
            headers={'apikey': settings.CURRENCY_CONVERTER_APIKEY}
        )

        currency_conversion_response = currency_conversion_request.json()

        self.to_eur = currency_conversion_response['rates']['EUR']
        self.to_usd = currency_conversion_response['rates']['USD']

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
