from fastapi import FastAPI
import subprocess

def ping(host: str):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping_route(host: str):
    # Validate and sanitize the input before using it in subprocess
    if not host.isalnum():
        return {'status': 'invalid', 'message': 'Invalid input'}
    return ping(host)