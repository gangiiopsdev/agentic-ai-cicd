from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_str):
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-.')
    return ''.join(c for c in input_str if c in allowed_chars)

@app.get("/ping")
def ping(host: str):
    # Sanitize user input
    host = sanitize_input(host)
    # Secure implementation using subprocess.run
    subprocess.run(['ping', host], check=True)
    return {"status": "completed"}