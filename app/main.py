from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate input to prevent command injection
    valid_hosts = ['example.com', 'localhost']  # Replace with actual validation logic
    if host not in valid_hosts:
        return {'error': 'Invalid host'}
    subprocess.run(['ping', host], check=True, capture_output=True)
    return {'status': 'completed'}