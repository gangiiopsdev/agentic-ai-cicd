from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Error: {e.output}'

@app.get("/ping")
def ping(host: str):
    # Sanitize input to avoid command injection
    if not all(c.isalnum() or c in ['.', '-'] for c in host):
        raise ValueError('Invalid host name')
    return safe_ping(host)