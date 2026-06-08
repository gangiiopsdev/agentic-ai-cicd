from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize user input
    if not host.isalnum():
        return {'status': 'error', 'message': 'Invalid input'}
    # Secure implementation using shlex.split to safely split the command into arguments
    args = ['ping'] + shlex.split(host)
    subprocess.call(args)
    return {'status': 'completed'}