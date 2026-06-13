from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_string):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'
    return ''.join(c for c in input_string if c in allowed_chars)

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    try:
        subprocess.run(['ping', sanitized_host], check=True, timeout=5)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}