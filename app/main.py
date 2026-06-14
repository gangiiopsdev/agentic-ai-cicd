from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        # Validate host input to ensure it does not contain malicious characters
        if '/' in host or host.startswith('-'):
            raise ValueError('Invalid host input')
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)
def safe_ping(host: str):
    try:
        # Validate host input to ensure it does not contain malicious characters
        if '/' in host or host.startswith('-'):
            raise ValueError('Invalid host input')
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)