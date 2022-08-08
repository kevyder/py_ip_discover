from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.database import Base
from app.main import app, get_db
from app.models import IPPermission

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base.metadata.create_all(bind=engine)


def override_get_db():
    try:
        db = TestingSession()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


def test_get_ip_allowed_info():
    response = client.get("/ip/45.238.183.189")
    assert response.status_code == 200


def test_get_ip_not_allowed_info():
    db = TestingSession()
    ip_record = IPPermission(ip_address='65.238.183.189', allowed=False)
    db.add(ip_record)
    db.commit()
    db.refresh(ip_record)

    response = client.get("/ip/65.238.183.189")
    assert response.status_code == 403


def test_get_invalid_ip_info():
    response = client.get("/ip/300.238.183.189")
    assert response.status_code == 422


def test_set_ip_restriction():
    response = client.post(
        "/set-ip-permissions/",
        json={"ip_address": "65.238.183.189", "allowed": False},
    )

    assert response.status_code == 200
