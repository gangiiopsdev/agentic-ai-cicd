from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str) -> dict:
    try:
        output = subprocess.check_output(['ping', host], shell=False, timeout=5)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}
    except subprocess.TimeoutExpired:
        return {'status': 'timeout', 'message': 'Ping request timed out'}

@app.get("/ping")
def ping(host: str):
    # Validate the host input to ensure it's safe
    if not host.strip():
        return {'status': 'error', 'message': 'Invalid host input'}
    return safe_ping(host)