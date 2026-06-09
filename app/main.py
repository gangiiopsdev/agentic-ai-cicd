from fastapi import FastAPI
import subprocess
import shlex
import re

allowed_hosts = ['example.com', 'test.com']

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate the input to ensure it does not contain malicious commands
    if not re.match(r'^[a-zA-Z0-9.-]+$', host) or host not in allowed_hosts:
        raise ValueError("Invalid input")
    result = subprocess.run(shlex.split('ping ' + host), capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}