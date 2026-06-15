from fastapi import FastAPI
import subprocess
import re

cmd_pattern = re.compile(r'^[a-zA-Z0-9.-]+$')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not cmd_pattern.match(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}