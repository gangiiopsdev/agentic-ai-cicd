from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize input
    if not host.isalnum():
        return {'status': 'error', 'message': 'Invalid input'}
    args = ['ping', host]
    subprocess.run(args)
    return {'status': 'completed'}