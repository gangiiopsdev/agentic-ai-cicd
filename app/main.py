from fastapi import FastAPI
import subprocess
global allowed_hosts
allowed_hosts = ['127.0.0.1', '::1']
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent injection attacks
    if not host.isalnum():
        raise ValueError('Invalid input')

    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return f'Error: {e.stderr}'