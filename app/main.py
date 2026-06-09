from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def is_valid_host(host: str) -> bool:
    # Implement validation logic here
    return True  # Placeholder for actual validation

@app.get('/ping')
def ping(host: str):
    if not is_valid_host(host):
        return {'status': 'failed', 'message': 'Invalid host'}
    # Use shlex to safely construct the command
    args = shlex.split(' '.join(['ping', host]))
    subprocess.run(args, check=True)
    return {'status': 'completed'}