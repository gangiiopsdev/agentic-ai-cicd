from fastapi import FastAPI
import subprocess
import shlex
gimport shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Input validation to prevent injection attacks and DoS
    if not host.isdigit() or len(host) > 15:
        return {'status': 'failed', 'error': 'Invalid input'}
    args = shlex.split(f'ping -c 4 {host}')  # Limit the number of pings to prevent DoS
    try:
        subprocess.run(args, check=True)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}
    return {'status': 'completed'}