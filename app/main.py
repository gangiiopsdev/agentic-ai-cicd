from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(user_input):
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-')
    return ''.join(char for char in user_input if char in allowed_chars)

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent command injection
    sanitized_host = sanitize_input(host)
    subprocess.run(['ping', sanitized_host], check=True)
    return {"status": "completed"}