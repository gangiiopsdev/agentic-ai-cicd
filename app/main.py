from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input_str):
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_')
    return ''.join(filter(allowed_chars.__contains__, input_str))

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if not sanitized_host:
        raise ValueError("Invalid host")
    subprocess.call(shlex.split(f"ping {sanitized_host}"), shell=False)
    return {"status": "completed"}