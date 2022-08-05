from pydantic import BaseModel


class HTTPError(BaseModel):
    detail: str

    class Config:
        schema_extra = {
            "example": {"detail": "HTTPException raised."},
        }


class IPinfo(BaseModel):
    country: str
    country_code: str
    city: str
    currency: str
    currency_to_usd: str
    currency_to_eur: str
