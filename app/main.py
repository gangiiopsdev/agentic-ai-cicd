from fastapi import FastAPI
import subprocess
import re

def execute_ping(host):
    # Validate the host input to ensure it is a valid hostname or IP address
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid host input')
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True, check=True)
    return result.stdout

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    output = execute_ping(host)
    return {'status': 'completed', 'output': output}