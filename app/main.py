from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(input_str):
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_.')
    return ''.join(filter(allowed_chars.__contains__, input_str))

def ping(host: str):
    sanitized_host = sanitize_input(host)
    subprocess.run(shlex.split(f'ping -c 1 {sanitized_host}'), check=True, capture_output=True, text=True)

app = FastAPI()

@app.get(
    "/",
    summary="Agentic Self-Healing Pipeline",
)
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get(
    "/ping",
    description="Ping a host using the provided hostname. Only alphanumeric characters and hyphens/underscores are allowed in the hostname.",
)
def ping(host: str):
    sanitized_host = sanitize_input(host)
    subprocess.run(shlex.split(f'ping -c 1 {sanitized_host}'), check=True, capture_output=True, text=True)
    return {"status": "completed"}