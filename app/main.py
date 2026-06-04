from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping_safe(host: str):
    try:
        # Use subprocess.run for a safer approach
        subprocess.run(['ping', host], check=True, capture_output=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping(host: str):
    return ping_safe(host)