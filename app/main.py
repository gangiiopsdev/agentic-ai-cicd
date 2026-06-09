from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    try:
        result = subprocess.run(['ping', '-c', '1', host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': e.stderr}

@app.get("/ping")
def ping_endpoint(host: str):
    # Validate the input to prevent injection attacks
    if not host.isalnum():
        return {'status': 'error', 'message': 'Invalid input'}
    return ping(host)