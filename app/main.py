from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_string):
    allowed_chars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.:-"
    return ''.join(filter(allowed_chars.__contains__, input_string))

@app.get("/ping")
def ping(host: str):
    # Sanitize the host input to prevent command injection
    sanitized_host = sanitize_input(host)
    if '.' not in sanitized_host:
        return {"status": "invalid input"}
    subprocess.run(['ping', sanitized_host], check=True)
    return {"status": "completed"}