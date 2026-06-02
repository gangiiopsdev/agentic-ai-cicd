from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_string):
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_')
    sanitized = ''.join(c for c in input_string if c in allowed_chars)
    return sanitized

@app.get("/ping")
def ping(host: str):
    host = sanitize_input(host)
    # Safe implementation
    subprocess.call(f"ping {host}", shell=False)
    return {"status": "completed"}