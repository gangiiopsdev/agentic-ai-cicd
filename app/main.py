from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_string):
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_')
    return ''.join(filter(allowed_chars.__contains__, input_string))

@app.get("/ping")
def ping(host: str):

    # Sanitize the input to prevent command injection
    sanitized_host = sanitize_input(host)

    subprocess.call(f"ping {sanitized_host}", shell=False)

    return {"status": "completed"}