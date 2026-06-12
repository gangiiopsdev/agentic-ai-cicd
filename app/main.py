from fastapi import FastAPI
import subprocess
import shlex
def validate_host(host):
    # Simple example of validation, replace with more robust logic as needed
    allowed_hosts = ['example.com', 'test.com']
    if host not in allowed_hosts:
        raise ValueError("Host is not allowed")
app = FastAPI()
@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
def ping(host: str):
    try:
        validate_host(host)
        command = ['ping', shlex.quote(host)]
        output = subprocess.run(command, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except ValueError as e:
        return {'status': 'failed', 'error': str(e)}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}