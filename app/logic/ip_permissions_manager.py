from app.database import Session
from app.models import IPPermission
from app.schemas import IPPermission as IPPermissionSchema


class IPPermissionsManager:

    def __init__(self, ip_address: str) -> None:
        self.ip_address = ip_address

    def __create_permissions(self, db: Session, allowed: bool) -> IPPermission:
        ip_record = IPPermission(ip_address=self.ip_address, allowed=allowed)
        db.add(ip_record)
        db.commit()
        db.refresh(ip_record)
        return ip_record

    def __update_permissions(
        self, db: Session, ip_record: IPPermission, allowed: bool
    ) -> IPPermission:
        setattr(ip_record, "allowed", allowed)
        db.add(ip_record)
        db.commit()
        db.refresh(ip_record)
        return ip_record

    def get_permissions(self, db: Session) -> IPPermission:
        return db.query(IPPermission).filter(IPPermission.ip_address == self.ip_address).first()

    def set_permissions(self, db: Session, allowed: bool) -> IPPermission:
        ip_record = self.get_permissions(db)
        if ip_record:
            self.__update_permissions(db, ip_record, allowed)
        else:
            self.__create_permissions(db, allowed)

        return IPPermissionSchema(ip_address=self.ip_address, allowed=allowed)
