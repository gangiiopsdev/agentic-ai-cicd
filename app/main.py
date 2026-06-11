from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Safe implementation without shell=True
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed: {e}'

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate input to prevent command injection
    if not host.isalnum():
        raise ValueError('Invalid input. Only alphanumeric characters are allowed.')
    return safe_ping(host)