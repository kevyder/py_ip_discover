from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.database import Session
from app.logic.ip_address_info import IPAddress
from app.logic.ip_permissions_manager import IPPermissionsManager
from app.schemas import HTTPError, IPinfo, IPPermission
from app.validators.ip_address_validator import IPAddressValidator


def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()


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
def get_ip_info(ip_address: str, db: Session = Depends(get_db)):
    IPAddressValidator(ip_address=ip_address).validate_ipv4()
    return IPAddress(ip_address).get_info()


@app.post("/set-ip-restriction/", responses={400: {"model": HTTPError}})
def set_ip_restriction(ip_permissions: IPPermission, db: Session = Depends(get_db)):
    ip_address = ip_permissions.ip_address
    allowed = ip_permissions.allowed
    IPAddressValidator(ip_address=ip_address).validate_ipv4()
    return IPPermissionsManager(ip_address=ip_address).set_permissions(db=db, allowed=allowed)
