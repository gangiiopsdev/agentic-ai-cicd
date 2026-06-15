from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed: {e}'

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not host.isalnum():  # Basic validation to prevent command injection
        return 'Invalid input'
    return safe_ping(host)