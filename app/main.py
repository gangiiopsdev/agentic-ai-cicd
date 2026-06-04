from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the host input
    if ' ' in host:
        return {'error': 'Invalid input'}

    # Fixed implementation
    subprocess.call(['ping', host])

    return {'status': 'completed'}