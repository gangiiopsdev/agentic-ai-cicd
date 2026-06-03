from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(value):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_.:()'
    return ''.join(filter(lambda x: x in allowed_chars, value))

@app.get("/ping")
def ping(host: str):

    # Sanitize input to prevent command injection
    sanitized_host = sanitize_input(host)

    # Use subprocess.run instead of subprocess.call with shell=True
    result = subprocess.run(['ping', sanitized_host], capture_output=True, text=True)

    return {'status': 'completed', 'output': result.stdout}