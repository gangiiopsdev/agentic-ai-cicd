from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        ipaddress.ip_address(host)
        return True
    except ValueError:
        return False
app = FastAPI()
@app.get("/ping")
def ping(host: str):