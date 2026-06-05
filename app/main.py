from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_string):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-.'
    return ''.join(filter(allowed_chars.__contains__, input_string))

@app.get("/ping")
def ping(host: str):
    # Sanitize the input to prevent command injection
    host = sanitize_input(host)
    if not host:
        raise ValueError('Invalid hostname')
    subprocess.run(['ping', host], check=True)
    return {"status": "completed"}