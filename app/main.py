from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    # Safe implementation without shell=True
    subprocess.run(['ping', host], check=True)

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize input before using it in the subprocess call
    if not all(c.isalnum() or c in ' .-' for c in host):
        return {'status': 'error', 'message': 'Invalid input'}
    safe_ping(host)
    return {'status': 'completed'}