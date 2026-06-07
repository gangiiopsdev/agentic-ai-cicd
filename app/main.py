from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(user_input):
    # Simple sanitization example: allow only alphanumeric characters and a few specific symbols
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_ '
    return ''.join(char for char in user_input if char in allowed_chars)

@app.get("/ping")
def ping(host: str):
    # Sanitize the input before using it with subprocess
    sanitized_host = sanitize_input(host)
    subprocess.call(['ping', sanitized_host], shell=False)
    return {"status": "completed"}