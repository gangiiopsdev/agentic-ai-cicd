from fastapi import FastAPI
import subprocess
import platform
def safe_ping(host: str):
    try:
        args = ['ping', host]
        if platform.system().lower() == 'windows':
            args.insert(1, '-n')
        result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate the host input to ensure it is a safe hostname or IP address
    if not validate_host(host):
        raise ValueError('Invalid host input')
    return safe_ping(host)

import re
def validate_host(host: str) -> bool:
    pattern = r'^[a-zA-Z0-9.-]{1,253}$'
    return re.match(pattern, host) is not None