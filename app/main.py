from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if not host.isdigit():
        raise ValueError('Invalid hostname')
    subprocess.call(['ping', host])

@app.get("/ping")
def ping(host: str):
    # Safer implementation
    try:
        safe_ping(host)
        return {'status': 'completed'}
    except ValueError as e:
        return {'error': str(e)}