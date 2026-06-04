from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def safe_ping(host: str) -> bool:
    # Validate input to prevent command injection
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return False
    try:
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f'Ping failed: {e}')
        return False

@app.get("/ping")
def ping(host: str):
    if safe_ping(host):
        return {"status": "completed"}
    else:
        raise ValueError('Invalid hostname')