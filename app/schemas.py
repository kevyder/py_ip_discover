from pydantic import BaseModel


class HTTPError(BaseModel):
    detail: str

    class Config:
        schema_extra = {
            "example": {"detail": "HTTPException raised."},
        }


class IPinfo(BaseModel):
    country: str
    iso: str
    currency: str
    currency_to_usd: float
