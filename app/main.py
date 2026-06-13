from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def run_ping(host):
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

def validate_host(host):
    pattern = re.compile(r'^[a-zA-Z0-9.-]+$')
    if not pattern.match(host):
        raise ValueError('Invalid input')

@app.get("/ping")
def ping(host: str):\n    try:\n        validate_host(host)\n        result = run_ping(host)\n        return {'status': 'completed', 'result': result}\n    except ValueError as e:\n        return {'status': 'error', 'result': str(e)}