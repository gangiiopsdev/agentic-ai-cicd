from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    try:
        # Safe implementation using subprocess.run with input validation
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'stdout': result.stdout.decode(), 'stderr': result.stderr.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping_host(host: str):
    # Validate input to prevent injection attacks
    if not host.isalnum():
        return {'status': 'failed', 'error': 'Invalid input'}
    return ping(host)