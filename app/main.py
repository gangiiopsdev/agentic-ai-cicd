from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate input to prevent RCE
    allowed_hosts = ['example.com', 'localhost']  # Define a whitelist of allowed hosts
    if host not in allowed_hosts:
        return {'status': 'error', 'message': 'Invalid host'}
    subprocess.run(['ping', host], capture_output=True, text=True)
    return {'status': 'completed'}