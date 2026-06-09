from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Sanitize the host input
    if 'ping' in host:
        return 'Invalid input'
    try:
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed: {e}'

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)