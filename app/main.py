from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    try:
        # Use subprocess.run instead of subprocess.call and avoid using shell=True
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

@app.get("/ping")
def ping_host(host: str):
    # Validate the input to ensure it does not contain malicious characters
    if any(char in host for char in [';', '&', '|', '*', '?', '<', '>', '^', '`']):
        return {'status': 'failed', 'error': 'Invalid input'}
    return ping(host)