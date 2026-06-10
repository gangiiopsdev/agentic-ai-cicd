from fastapi import FastAPI
import subprocess
def sanitize_input(input_string):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(char for char in input_string if char in allowed_chars)

def is_safe_host(host):
    safe_hosts = ['example.com', 'another.example.com']  # Add more safe hosts as needed
    return host in safe_hosts

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        raise ValueError("Host is not allowed")
    sanitized_host = sanitize_input(host)
    subprocess.run(['ping', sanitized_host], check=True, shell=False)
    return {"status": "completed"}