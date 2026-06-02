from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation using subprocess.run with shell=False and list arguments
    subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize input before passing to the function
    if not host.isalnum():
        return {'error': 'Invalid input'}, 400

    safe_ping(host)

    return {"status": "completed"}