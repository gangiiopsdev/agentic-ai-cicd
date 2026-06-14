from fastapi import FastAPI
import subprocess
def sanitize_input(user_input):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(filter(allowed_chars.__contains__, user_input))

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize input
    sanitized_host = sanitize_input(host)
    if not sanitized_host:
        raise ValueError("Invalid input")
    # Secure implementation
    subprocess.run(['ping', sanitized_host], capture_output=True, text=True)
    return {"status": "completed"}