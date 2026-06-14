from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize input
    if not host.isalnum():
        return {'error': 'Invalid host'}

    args = ['ping', host]
    subprocess.run(args, check=True)

    return {'status': 'completed'}