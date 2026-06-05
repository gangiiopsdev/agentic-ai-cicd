from fastapi import FastAPI
import subprocess
cimport = __import__

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate the host input to prevent command injection
    if not host.isalnum():
        return {'status': 'error', 'message': 'Invalid input'}
    command = ['ping', host]
    subprocess.run(command, check=True)  # Use subprocess.run with shell=False and check=True for better security
    return {'status': 'completed'}