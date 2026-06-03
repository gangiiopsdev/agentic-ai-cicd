from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize the host input to prevent command injection
    if not host.isalnum():
        return {'error': 'Invalid input'}
    subprocess.run(['ping', host], check=True)
    return {'status': 'completed'}