from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Validate and sanitize input
    if not host.isalnum():
        return {'status': 'failed', 'error': 'Invalid host name'}
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping_host(host: str):
    return ping(host)