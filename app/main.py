from fastapi import FastAPI
import subprocess
cimport ipaddress

app = FastAPI()

def validate_host(host):
    try:
        return ipaddress.ip_address(host)
    except ValueError:
        raise ValueError('Invalid IP address')

@app.get("/ping")
def ping(host: str):  
    host = validate_host(host)
    # Safe implementation
    subprocess.call(['ping', str(host)])
    return {"status": "completed"}