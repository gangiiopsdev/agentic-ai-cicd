from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_valid_host(host):
    # Simple validation for demonstration purposes
    return host.strip().replace('.', '').isalnum()

def sanitize_input(input_str):
    safe_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'
    return ''.join(c for c in input_str if c in safe_chars)

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(sanitize_input(host)):
        raise ValueError('Invalid host')
    command = ['ping', '-c', '1']  # Use specific options to mitigate risks
    subprocess.run(command, args=[host], check=True)
    return {"status": "completed"}