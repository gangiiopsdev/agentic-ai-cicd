from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_ping(host):
    try:
        result = subprocess.run(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Error: {e.stderr}'

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return 'Invalid host'
    return execute_ping(host)

def validate_host(host):
    # Simple validation to ensure the host is safe (e.g., does not contain malicious characters)
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-')
    return all(c in allowed_chars for c in host)