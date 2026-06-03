from fastapi import FastAPI
import subprocess
def sanitize_input(input_str):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'-.'
    return ''.join(c for c in input_str if c in allowed_chars)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if not sanitized_host.isalnum():
        raise ValueError("Invalid input")
    subprocess.call(['ping', sanitized_host], shell=False)
    return {"status": "completed"}