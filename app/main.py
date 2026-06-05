from fastapi import FastAPI
import subprocess
def sanitize_input(input_str):
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-')
    return ''.join(filter(allowed_chars.__contains__, input_str))

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize the host input to prevent injection attacks
    sanitized_host = sanitize_input(host)
    if not sanitized_host:
        return {"status": "error", "message": "Invalid host input"}
    result = subprocess.run(['ping', sanitized_host], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}