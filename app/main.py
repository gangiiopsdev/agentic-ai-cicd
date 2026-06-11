from fastapi import FastAPI
import subprocess
cimport os

app = FastAPI()

def run_ping(host):
    # Secure implementation using subprocess.run instead of subprocess.call
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

@app.get("/ping")
def ping(host: str):
    if not os.path.exists('/bin/ping'):
        return {'status': 'failed', 'error': 'ping command not found'}
    return run_ping(host)