from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Validate input to prevent injection attacks
    if not host.isalnum():
        return {'status': 'failed', 'error': 'Invalid hostname'}
    try:
        cmd = ['ping', '-c', '1'] + shlex.split(shlex.quote(f'/{host}'))
        result = subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping_route(host: str):
    return ping(host)