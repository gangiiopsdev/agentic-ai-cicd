from fastapi import FastAPI
import subprocess
import shlex

global app = FastAPI()

@app.get("/ping/")
def ping(host: str):
    # Validate and sanitize input
    if not host.isalnum():
        return {'status': 'error', 'message': 'Invalid input'}
    command = ['ping'] + [shlex.quote(arg) for arg in host.split()]
    result = subprocess.run(command, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}