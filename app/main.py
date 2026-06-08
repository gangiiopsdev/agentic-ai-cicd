from fastapi import FastAPI
import subprocess
import shlex
import requests
timeout_duration = 10  # Set a reasonable timeout duration

app = FastAPI()

def validate_host(host):
    response = requests.get(f'https://api.ipify.org?domain={host}', timeout=timeout_duration)
    if not response.status_code == 200:
        raise ValueError('Invalid host')

@app.get("/ping")
def ping(host: str):
    validate_host(host)
    # Secure implementation using subprocess.run with shell=False and quoting arguments
    result = subprocess.run(['ping', shlex.quote(host)], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}