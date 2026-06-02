from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize input
    if not host.isalnum():
        raise ValueError('Invalid hostname')
    command = ['ping', subprocess.list2cmdline([host])]
    subprocess.run(command, check=True)
    return {'status': 'completed'}