from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed: {e}'

@app.get("/ping")
def ping(host: str):
    # Validate the input to prevent command injection
    if not host.isalnum():
        raise ValueError('Invalid input')
    return safe_ping(host)