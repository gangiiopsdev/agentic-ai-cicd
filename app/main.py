from fastapi import FastAPI
import subprocess
from shlex import quote
def sanitize_input(input_str):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(filter(lambda char: char in allowed_chars, input_str))

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = quote(sanitize_input(host), safe=':/')
    subprocess.run(['ping', '-c 1', sanitized_host], check=True)
    return {"status": "completed"}