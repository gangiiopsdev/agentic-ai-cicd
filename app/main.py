from fastapi import FastAPI
import subprocess
cimport os

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Sanitize input to prevent command injection
    if host.strip().isdigit() and int(host) >= 1 and int(host) <= 254:
        safe_host = str(int(host))  # Ensure host is an integer
        subprocess.run(['ping', '-c', '4', safe_host], check=True, capture_output=True, text=True)
    else:
        return {'error': 'Invalid host'}

    return {'status': 'completed'}