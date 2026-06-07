from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def sanitize_input(input_str):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'
    sanitized = ''.join(c for c in input_str if c in allowed_chars)
    return sanitized

@app.get("/ping")
def ping(host: str):
    sanitized_host = quote(sanitize_input(host))
    subprocess.run(['ping', sanitized_host], check=True)
    return {"status": "completed"}