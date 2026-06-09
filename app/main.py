from fastapi import FastAPI
import subprocess

def sanitize_input(input_string):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-.:'
    return ''.join(char for char in input_string if char in allowed_chars)

def validate_host(host: str):
    valid_hosts = ['google.com', 'example.com']  # Example list of allowed hosts
    return host in valid_hosts

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        raise ValueError("Invalid host")
    sanitized_host = sanitize_input(host)
    result = subprocess.run(['ping', sanitized_host], capture_output=True, text=True, shell=False)
    return {'output': result.stdout}