from fastapi import FastAPI
import subprocess

app = FastAPI()

def secure_ping(host: str):
    # Validate the host to ensure it's a safe input (e.g., using regex)
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid host name')

@app.get('/ping')
def ping(host: str):
    secure_ping(host)
    subprocess.run(['ping', host], check=True)
    return {'status': 'completed'}