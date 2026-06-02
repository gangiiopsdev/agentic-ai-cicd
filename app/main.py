from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host):
    try:
        # Use subprocess.run for a safer and more flexible solution
        args = ['ping'] + shlex.split(host)
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

global app
app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate the host input to ensure it's safe before executing the command
    if not validate_host(host):
        return {'status': 'error', 'result': 'Invalid host'}
    status = safe_ping(host)
    return {'status': 'completed', 'result': status}
def validate_host(host: str) -> bool:
    # Example validation: allow only alphanumeric characters and a few special characters
    import re
    return re.match(r'^[a-zA-Z0-9.-]{1,255}$', host) is not None