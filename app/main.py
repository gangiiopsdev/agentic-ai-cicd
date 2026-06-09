from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_str):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'
    return ''.join(filter(lambda x: x in allowed_chars, input_str))

def safe_ping(host: str):
    if not host or len(host) > 255:
        raise ValueError("Invalid host")
    subprocess.call(["ping", host])

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    safe_ping(sanitized_host)
    return {"status": "completed"}