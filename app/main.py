from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Validate the input to prevent injection attacks
    if not host.strip().isalnum():
        raise ValueError('Invalid hostname')
    result = subprocess.run(shlex.split(f'ping {host}'), capture_output=True, text=True, check=True)
    return {'status': 'completed', 'output': result.stdout}

@app.get("/ping")
def ping_route(host: str):
    return ping(host)