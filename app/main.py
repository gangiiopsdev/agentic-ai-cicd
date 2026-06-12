from fastapi import FastAPI
import subprocess

global app = FastAPI()

def safe_ping(host: str):
    try:
        # Sanitize input by escaping or validating the host parameter
        output = subprocess.run(['ping', '-c', '1', '--'] + [subprocess.list2cmdline([host])], capture_output=True, text=True, check=False)
        return output.stdout or output.stderr
    except Exception as e:
        return str(e)

def get_safe_ping(host: str):
    result = safe_ping(host)
    return {'status': 'completed', 'result': result}

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate the host parameter to ensure it does not contain malicious input
    if any(char in host for char in [';', '|', '&', '*', '$', '`', '>', '<']):
        return {'status': 'error', 'message': 'Invalid host parameter'}
    return get_safe_ping(host)