from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate the host input to prevent injection attacks
    allowed_hosts = ['example.com', 'test.com']
    if host not in allowed_hosts:
        return {'status': 'denied'}
    # Use a safer method to execute commands, avoiding shell=True and subprocess.call()
    subprocess.run(['ping', host], check=True)
    return {'status': 'completed'}