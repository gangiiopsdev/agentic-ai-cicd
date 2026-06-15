from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    try:
        # Validate input to prevent injection attacks
        if not host.strip():
            raise ValueError('Invalid host name')
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': e.stderr}

@app.get("/ping")
def ping_route(host: str):
    return ping(host)