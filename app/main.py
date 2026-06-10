from fastapi import FastAPI
import subprocess
cimport os

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Sanitize input to prevent command injection
    if host.strip().isdigit() and int(host) >= 1 and int(host) <= 254:
        subprocess.run(['ping', host], check=True, capture_output=True, text=True)
    else:
        return {'error': 'Invalid host'}

    return {'status': 'completed'}