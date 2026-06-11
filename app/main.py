from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Sanitize input to prevent injection
    if not host.isalnum():
        return {'status': 'error', 'output': 'Invalid input'}
    try:
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': str(e)}

@app.get("/ping")
def ping_endpoint(host: str):
    # Sanitize input to prevent injection
    if not host.isalnum():
        return {'status': 'error', 'output': 'Invalid input'}
    return ping(host)