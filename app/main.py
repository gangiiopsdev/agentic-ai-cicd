from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    if '.' in host or ':' in host:
        return False
    return True

@app.get('/ping')
def ping(host: str):
    if not safe_ping(host):
        return {'status': 'error', 'message': 'Invalid host'}
    # Fixed implementation using shlex to safely handle command arguments and subprocess.run for better security
    args = shlex.split(f'ping {host}')
    result = subprocess.run(args, check=True, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}