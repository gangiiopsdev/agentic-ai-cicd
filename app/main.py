from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_str):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    sanitized = ''.join(char for char in input_str if char in allowed_chars)
    return sanitized

@app.get("/ping")
def ping(host: str):

    # Sanitize input to prevent command injection
    host = sanitize_input(host)

    # Safe implementation using subprocess.run with args
    result = subprocess.run(['ping', host], capture_output=True, text=True)

    return {'status': 'completed', 'output': result.stdout}