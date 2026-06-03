from fastapi import FastAPI
import subprocess
cimport os

app = FastAPI()

def safe_ping(host: str):
    args = ['ping', host]
    try:
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': e.stderr}

@app.get("/ping")
def ping(host: str):
    # Sanitize user input
    if not host.strip().isalnum():
        return {'status': 'error', 'output': 'Invalid host name'}
    return safe_ping(host)