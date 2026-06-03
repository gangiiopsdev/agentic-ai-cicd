from fastapi import FastAPI
import subprocess
import shlex

def safe_ping(host: str):
    if not host.isalnum():
        raise ValueError("Invalid hostname")
    try:
        command = ['ping', '-c', '1', shlex.quote(host)]
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': str(e)}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate the host to ensure it is a valid hostname or IP address
    import re
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):  # Simple regex for demonstration purposes
        raise ValueError("Invalid hostname")
    return safe_ping(host)