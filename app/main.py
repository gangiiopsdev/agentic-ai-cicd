from fastapi import FastAPI
import subprocess
import re
class Sanitize:
    @staticmethod
def sanitize_host(host: str):
        return re.sub(r'[^a-zA-Z0-9.-]', '', host)

app = FastAPI()

def ping(host: str):
    sanitized_host = Sanitize.sanitize_host(host)
    if not sanitized_host:
        raise ValueError('Invalid hostname')
    subprocess.run(['ping', '-c 1', sanitized_host], check=True)

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)