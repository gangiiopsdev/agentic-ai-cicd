from fastapi import FastAPI
import subprocess
from typing import Optional

app = FastAPI()

def safe_ping(host: str) -> dict:
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}

@app.get("/ping")
def ping(host: str) -> dict:
    if not host.isascii() or not all(c in string.printable for c in host):
        return {'status': 'error', 'message': 'Invalid input'}
    return safe_ping(host)