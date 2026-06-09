from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Validate host input
    if not host.isalnum():
        return {'status': 'error', 'message': 'Invalid host'}
    subprocess.run(['ping', host], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    return {'status': 'completed'}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)