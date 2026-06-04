from fastapi import FastAPI
import subprocess

def safe_ping(host):
    # Sanitize the host input to prevent command injection
    if not host.isalnum():
        raise ValueError('Invalid host input')
    result = subprocess.run(['ping', '-c', '1', host], check=True, capture_output=True, text=True)
    return {'status': 'completed', 'result': result.stdout}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        result = safe_ping(host)
        return result
    except ValueError as e:
        return {'status': 'error', 'message': str(e)}