from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.logic.ip_address_info import IPAddress
from app.schemas import HTTPError, IPinfo
from app.validators.ip_address_validator import IPAddressValidator


def get_application():
    _app = FastAPI(title=settings.PROJECT_NAME)

    _app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return _app


app = get_application()


@app.get("/ip/{ip_address}", responses={200: {"model": IPinfo}, 400: {"model": HTTPError}})
def get_ip_info(ip_address: str):
    IPAddressValidator(ip_address=ip_address).validate_ipv4()
    return IPAddress(ip_address).get_info()
