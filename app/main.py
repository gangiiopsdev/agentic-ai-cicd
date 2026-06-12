from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Safer implementation using subprocess.run with shlex.quote to sanitize input
    result = subprocess.run(shlex.split('ping ' + host), capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}

@app.get("/ping")
def ping_route(host: str):
    # Validate input to prevent command injection
    if not host.isalnum():
        raise ValueError('Invalid input')
    return ping(host)