from fastapi import FastAPI
import subprocess
from shlex import quote as cmd_quote

app = FastAPI()

def is_safe_host(host: str) -> bool:
    return all(char.isalnum() for char in host)

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        return {'error': 'Invalid host input'}
    subprocess.call(["ping", cmd_quote(host)])
    return {"status": "completed"}