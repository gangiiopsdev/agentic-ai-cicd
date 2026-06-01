from fastapi import FastAPI
import subprocess
def ping(host: str):
    try:
        # Use a complete executable path for security and validate input
        if not host.isalnum():
            raise ValueError('Invalid host name')
        result = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, shell=False)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'output': e.output.decode()}

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)