from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_str):
    allowed_chars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-")
    return ''.join(filter(allowed_chars.__contains__, input_str))

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    # Safe implementation using subprocess.run with input sanitization
    result = subprocess.run(['ping', sanitized_host], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}