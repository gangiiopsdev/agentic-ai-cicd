from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Validate host input to prevent command injection
    if not host.isalnum():
        return {'status': 'failed', 'error': 'Invalid host input'}
    try:
        subprocess.run(['ping', host], check=True)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}
    return {'status': 'completed'}

@app.get("/ping")
def ping_wrapper(host: str):
    return ping(host)