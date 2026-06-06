from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Secure implementation using subprocess.run with argument splitting
    try:
        result = subprocess.run(shlex.split(f'ping {host}'), check=True)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping_route(host: str):
    # Sanitize input to prevent injection attacks
    if not all(c.isalnum() or c in '-.' for c in host):
        return {'status': 'failed', 'error': 'Invalid hostname'}
    return ping(host)