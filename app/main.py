from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate input
    if not host.isalnum():
        return {'status': 'error', 'message': 'Invalid input'}
    command = ['ping'] + shlex.split(host)
    # Use a safe method to execute the command
    subprocess.run(command, check=True)
    return {'status': 'completed'}