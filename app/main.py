from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_str):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'
    return ''.join(filter(allowed_chars.__contains__, input_str))

@app.get("/ping")
def ping(host: str):
    # Sanitize input to avoid injection attacks
    sanitized_host = sanitize_input(host)
    subprocess.run(['ping', sanitized_host], check=True)
    return {"status": "completed"}