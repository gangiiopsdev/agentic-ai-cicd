from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Validate input to prevent injection attacks
    if not host.strip() or len(host) > 256:
        raise ValueError("Invalid host name")
    try:
        result = subprocess.run(shlex.split(f'ping -c 1 {host}'), check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': e.stderr.decode()}

@app.get("/ping")
def ping_route(host: str):
    return ping(host)