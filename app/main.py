from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize user input
    if not host.isalnum():
        return {'status': 'error', 'message': 'Invalid input'}
    # Secure implementation
    subprocess.call(['ping', host])
    return {'status': 'completed'}