from fastapi import FastAPI
import subprocess
import re
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
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    try:
        validate_host(host)
        result = run_ping(host.replace('.', ' ').replace('-', ' '))  # sanitize host to prevent command injection
        return {'status': 'completed', 'result': result}
    except ValueError as e:
        return {'status': 'error', 'result': str(e)}