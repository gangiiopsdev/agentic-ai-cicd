from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

# Regular expression to validate host input
def is_valid_host(host: str) -> bool:
    return re.match(r'^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$|^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$', host)

def ping(host: str):
    if not is_valid_host(host):
        return {'status': 'failed', 'error': 'Invalid host format'}
    try:
        output = subprocess.run(['ping', '-c', '4', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping_route(host: str):
    return ping(host)