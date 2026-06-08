from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation using subprocess.run
    try:
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed with error: {e.stderr}'

@app.get("/ping")
def ping(host: str):
    # Validate input to prevent command injection
    if not host.isalnum():
        raise ValueError('Invalid input for ping')
    response = safe_ping(host)
    return {'status': 'completed', 'response': response}