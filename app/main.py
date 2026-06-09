from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_string):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'
    return ''.join(char for char in input_string if char in allowed_chars)

@app.get("/ping")
def ping(host: str):
    safe_host = sanitize_input(host)
    subprocess.run(['ping', safe_host], check=True)
    return {"status": "completed"}