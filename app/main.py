from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping_endpoint(host: str):
    # Validate host input to prevent injection attacks
    if not host.isdigit():
        return {'status': 'failed', 'error': 'Invalid host'}
    return ping(host)