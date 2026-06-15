from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Validate host input to prevent shell injection
    if not host.strip():
        return {'status': 'error', 'message': 'Invalid host'}

    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'success', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': e.stderr}

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)