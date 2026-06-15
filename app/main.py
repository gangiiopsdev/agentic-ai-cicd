from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    # Simple validation example: allow only alphanumeric characters and hyphens
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-')
    return all(c in allowed_chars for c in host)

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {"status": "invalid host"}, 400
    subprocess.run(['ping', host], check=True)
    return {"status": "completed"}