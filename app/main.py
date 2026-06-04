from fastapi import FastAPI
import subprocess
def safe_ping(host):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Error: {e}'

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent code injection
    if not host.isalnum():
        return {'status': 'error', 'response': 'Invalid host name'}
    response = safe_ping(host)
    return {'status': 'completed', 'response': response}