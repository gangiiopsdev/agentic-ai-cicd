from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def sanitize_input(value):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'
    return ''.join(filter(allowed_chars.__contains__, value))

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    args = ['ping', quote(sanitized_host)]
    subprocess.run(args, check=True)
    return {"status": "completed"}