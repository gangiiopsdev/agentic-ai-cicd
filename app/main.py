from fastapi import FastAPI
import subprocess
import shlex

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
    command = ['ping'] + shlex.split(sanitized_host)
    subprocess.run(command, check=True)
    return {"status": "completed"}