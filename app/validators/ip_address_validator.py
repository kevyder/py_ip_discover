import re

from fastapi import HTTPException


class IPAddressValidator:

    IPV4_PATTERN = r'''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(
                        25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(
                        25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(
                        25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$'''

    def __init__(self, ip_address):
        self.ip_address = ip_address

    def validate_ipv4(self):
        if not re.search(self.IPV4_PATTERN, self.ip_address):
            raise HTTPException(status_code=422, detail="Invalid IP address")
        return True
