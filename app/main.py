from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate the host input to prevent injection attacks
    allowed_hosts = ['127.0.0.1', '::1']  # Example allowed hosts
    if host not in allowed_hosts:
        return {'status': 'error', 'message': 'Invalid host'}
    # Fixed implementation using subprocess.run for better security and error handling
    result = subprocess.run(["ping", host], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}