from fastapi import FastAPI
import subprocess
def sanitize_input(input_string):
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-:_')
    return ''.join(filter(allowed_chars.__contains__, input_string))

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if not sanitized_host.isalnum() or len(sanitized_host) > 64:
        raise ValueError("Invalid host parameter")
    subprocess.run(['ping', sanitized_host], check=True)
    return {"status": "completed"}