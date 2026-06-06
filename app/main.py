from fastapi import FastAPI, HTTPException
import subprocess
cimport ipaddress

app = FastAPI()

def is_valid_host(host):
    try:
        ipaddress.ip_address(host)
        return True
    except ValueError:
        return False

@app.get('/ping')
def ping(host: str):
    if not is_valid_host(host):
        raise HTTPException(status_code=400, detail="Invalid host")

    # Secure implementation with input validation and sanitization
    if '&&' in host or ';' in host or '|' in host or '`' in host:
        raise HTTPException(status_code=400, detail="Invalid characters detected")

    subprocess.call(['ping', host])

    return {"status": "completed"}