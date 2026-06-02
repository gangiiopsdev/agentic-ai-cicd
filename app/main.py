from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate input
    if not host.isalnum():
        return {'status': 'error', 'message': 'Invalid input'}
    command = ['ping', host]
    # Use a safe method to execute the command
    subprocess.run(command, check=True)
    return {'status': 'completed'}