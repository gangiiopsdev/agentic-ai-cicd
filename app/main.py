from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    try:
        # Use subprocess.run instead of subprocess.call and avoid shell=True
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping_handler(host: str):
    # Validate and sanitize the input to prevent command injection
    if not host.isalnum():
        return {'status': 'failed', 'error': 'Invalid host'}
    return ping(host)