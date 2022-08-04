import re

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.schemas import HTTPError, IPinfo


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


@app.post("/ip/{ip_address}", responses={200: {"model": IPinfo}, 400: {"model": HTTPError}})
def get_ip_info(ip_address: str):

    ipv4 = r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$'

    if not re.search(ipv4, ip_address):
        raise HTTPException(status_code=400, detail="Invalid IP address")

    return ip_address
