from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    args = ['ping', host]
    subprocess.run(args, check=True)

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if not is_safe_host(host):
        raise HTTPException(status_code=400, detail="Invalid host")
    safe_ping(host)
    return {"status": "completed"}

import ipaddress

def is_safe_host(host: str):
    try:
        ip_address = ipaddress.ip_address(host)
        if isinstance(ip_address, (ipaddress.IPv4Address, ipaddress.IPv6Address)):
            return True
    except ValueError:
        pass
    return False