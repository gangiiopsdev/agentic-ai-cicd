from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if not host.isalnum():
        raise ValueError('Invalid hostname')
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        if not host.isalnum():
            raise ValueError('Invalid hostname')
        return safe_ping(host)
    except ValueError as e:
        return {'status': 'failed', 'error': str(e)}