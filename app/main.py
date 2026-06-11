from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_string):
    allowed_characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    sanitized = ''.join(char for char in input_string if char in allowed_characters)
    return sanitized

@app.get("/ping")
def ping(host: str):
    # Sanitize the input to prevent command injection
    safe_host = sanitize_input(host)

    # Use a safe subprocess call without shell=True
    result = subprocess.call(["ping", safe_host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}