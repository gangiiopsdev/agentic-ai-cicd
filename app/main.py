from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_str):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(char for char in input_str if char in allowed_chars)

@app.get("/ping")
def ping(host: str):

    # Sanitize input
    sanitized_host = sanitize_input(host)

    # Use subprocess.run without shell=True
    result = subprocess.run(['ping', sanitized_host], capture_output=True, text=True)

    return {'status': 'completed', 'output': result.stdout}