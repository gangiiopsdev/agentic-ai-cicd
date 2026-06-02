from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Sanitize input to prevent command injection
    if not host.isalnum():
        raise ValueError('Invalid input')
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'stdout': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}

@app.get("/ping")
def ping_endpoint(host: str):
    try:
        # Sanitize input to prevent command injection
        if not host.isalnum():
            raise ValueError('Invalid input')
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'stdout': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}