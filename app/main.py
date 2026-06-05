from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if not host.isalnum():
        raise ValueError('Invalid host name')

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    # Safe implementation using subprocess.run with a full path to avoid potential shell injection
    result = subprocess.run(['/bin/ping', host], capture_output=True, text=True, check=True)
    return {'status': 'completed', 'output': result.stdout}