from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_string):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    sanitized_string = ''.join(char for char in input_string if char in allowed_chars)
    return sanitized_string

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    # Secure implementation using subprocess.run with shell=False
    result = subprocess.run(['ping', sanitized_host], capture_output=True, text=True, check=False)
    return {'status': 'completed', 'output': result.stdout}