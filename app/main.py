from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host: str):
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-._')
    if not all(c in allowed_chars for c in host):
        raise ValueError('Invalid host name')

@app.get("/ping")
def ping(host: str):
    validate_host(host)
    args = ['ping', '-c', '1', host]
    result = subprocess.run(args, capture_output=True, text=True, check=True)
    return {"status": "completed", "output": result.stdout}