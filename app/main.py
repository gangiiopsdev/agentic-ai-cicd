from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Sanitize input to prevent shell injection
    if 'ping' in host or ';' in host or '&amp;' in host:
        return {'status': 'error', 'message': 'Invalid host provided'}
    result = subprocess.run(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return {'status': 'completed', 'stdout': result.stdout, 'stderr': result.stderr}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)