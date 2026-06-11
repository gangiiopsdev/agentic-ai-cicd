from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent shell injection
    if any(char in host for char in ['&', '|', ';', '`', '\\']):
        return {'status': 'failed', 'error': 'Invalid characters in hostname'}
    return safe_ping(host)