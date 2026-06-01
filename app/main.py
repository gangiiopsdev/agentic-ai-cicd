from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    args = ['ping', host]
    result = subprocess.run(args, check=True, capture_output=True, text=True)
    return result.stdout

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if not is_safe_host(host):
        raise HTTPException(status_code=400, detail="Invalid host")
    output = safe_ping(host)
    return {"status": "completed", "output": output}

import ipaddress

def is_safe_host(host: str):
    try:
        ip_address = ipaddress.ip_address(host)
        if isinstance(ip_address, (ipaddress.IPv4Address, ipaddress.IPv6Address)):
            return True
    except ValueError:
        pass
    return False