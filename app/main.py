from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if any(char in host for char in [';', '&', '|', '`']):
        raise ValueError('Unsafe characters detected in hostname')
    subprocess.run(['ping', host], check=True, capture_output=True)

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}