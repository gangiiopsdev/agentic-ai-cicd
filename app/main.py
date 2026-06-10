from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation with input validation
    if not host or not host.isalnum():
        return {'status': 'error', 'message': 'Invalid input'}
    args = shlex.split(f'ping {host}')
    try:
        subprocess.run(args, check=True)
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}
    return {'status': 'completed'}