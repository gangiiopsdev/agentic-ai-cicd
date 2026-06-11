from fastapi import FastAPI
import re
import shlex
g import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the host input
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid hostname')
    result = subprocess.run(['ping', '-c', '1'] + shlex.split(host), check=True, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}