from pydantic import BaseModel


class HTTPError(BaseModel):
    status_code: int
    detail: str

    class Config:
        schema_extra = {
            "example": {
                "status_code": "400",
                "detail": "HTTPException raised."
            },
        }


class IPinfo(BaseModel):
    country: str
    country_code: str
    city: str
    currency: str
    currency_to_usd: str
    currency_to_eur: str

    class Config:
        schema_extra = {
            "example": {
                "country": "Colombia",
                "country_code": "CO",
                "city": "Bogota",
                "currency": "COP",
                "currency_to_usd": "0.0003",
                "currency_to_eur": "0.0002",
            },
        }


class IPPermission(BaseModel):
    ip_address: str
    allowed: bool

    class Config:
        orm_mode = True

        schema_extra = {
            "example": {
                "ip_address": "200.255.255.255",
                "allowed": False
            },
        }
