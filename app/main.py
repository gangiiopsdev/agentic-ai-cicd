from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_str):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-:_'
    sanitized = ''.join(char for char in input_str if char in allowed_chars)
    return sanitized

@app.get("/ping")
def ping(host: str):
    host = sanitize_input(host)
    subprocess.run(['ping', host], check=True)
    return {"status": "completed"}