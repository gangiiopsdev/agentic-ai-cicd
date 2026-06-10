from fastapi import FastAPI
import subprocess
def safe_ping(host):
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_.')
    if host and all(c in allowed_chars for c in host):
        return True
    return False

app = FastAPI()

@app.get("/ping")
def ping(host: str):