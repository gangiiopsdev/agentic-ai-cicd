from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize the input to prevent command injection
    if not host.isalnum():
        return {'status': 'error', 'message': 'Invalid input'}
    command = ['ping', shlex.quote(host)]
    subprocess.run(command, check=True)
    return {'status': 'completed'}