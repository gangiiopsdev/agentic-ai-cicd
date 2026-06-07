from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    try:
        response = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': response.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode('utf-8')}

@app.get("/ping")
def ping(host: str):
    # Validate the host input to ensure it is safe
    if not validate_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    return safe_ping(host)

def validate_host(host: str) -> bool:
    # Implement a simple validation logic, e.g., check for allowed characters and patterns
    allowed_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-"
    return all(char in allowed_chars for char in host)