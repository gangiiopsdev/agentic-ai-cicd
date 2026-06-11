from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Secure implementation
    if not host:
        return {'status': 'failed', 'error': 'Empty host provided'}
    args = shlex.split(f'ping {host}')
    try:
        result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}

@app.get("/ping")
def ping_route(host: str):
    return ping(host)