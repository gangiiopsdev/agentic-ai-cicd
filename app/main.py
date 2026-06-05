from fastapi import FastAPI
import subprocess
cimport ipaddress

app = FastAPI()

def is_valid_host(host):
    try:
        ipaddress.ip_address(host)
        return True
    except ValueError:
        return False

@app.get="/ping")
def ping(host: str):
    if not is_valid_host(host):
        raise HTTPException(status_code=400, detail="Invalid host")

    # Secure implementation
    subprocess.call(['ping', host])

    return {"status": "completed"}