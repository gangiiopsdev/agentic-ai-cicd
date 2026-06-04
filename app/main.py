from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Use a whitelist or validation to ensure safe input
    if not host.isdigit():
        raise ValueError('Invalid host')
    subprocess.call(['ping', host])

@app.get("/ping")
def ping(host: str):
    try:
        safe_ping(host)
    except ValueError as e:
        return {'error': str(e)}
    return {'status': 'completed'}