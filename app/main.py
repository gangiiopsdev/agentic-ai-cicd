from fastapi import FastAPI
import subprocess
import shlex

def ping(host: str):
    # Validate input to prevent injection attacks
    if not host.replace('.', '').replace('-', '').isalnum():
        return {'status': 'error', 'message': 'Invalid host'}
    try:
        args = ['ping', '-c', '1'] + shlex.split(host)
        result = subprocess.run(args, check=True, stdout=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}

app = FastAPI()

@app.get('/ping')
def ping_endpoint(host: str):
    return ping(host)