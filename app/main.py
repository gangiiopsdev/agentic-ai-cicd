from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, shell=False)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_route(host: str):
    # Validate host input to ensure it's safe for use in a command
    if not is_safe_hostname(host):
        return {'status': 'failed', 'error': 'Invalid hostname'}
    return ping(host)

# Example function to validate the hostname
def is_safe_hostname(hostname: str) -> bool:
    # Add your validation logic here, e.g., regex matching against allowed characters and patterns
    import re
    pattern = r'^[a-zA-Z0-9.-]+$'
    return bool(re.match(pattern, hostname))