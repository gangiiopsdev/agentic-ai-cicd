from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize input
    if not host.isalnum():
        return {'status': 'error', 'message': 'Invalid host'}

    args = ['ping', host]
    subprocess.run(args, check=True, capture_output=True, text=True)

    return {'status': 'completed'}