from fastapi import FastAPI
import subprocess
from typing import List, AnyStr

app = FastAPI()

def safe_ping(host: AnyStr):
    # Sanitize host input to prevent command injection
    if not all(c.isalnum() or c in ['.', '-', '_'] for c in host.replace(' ', '')):
        raise ValueError('Invalid host name')
    subprocess.run(['ping', '-c', '1', host], check=True, shell=False)

@app.get("/ping")
def ping(host: str):
    safe_ping(host)