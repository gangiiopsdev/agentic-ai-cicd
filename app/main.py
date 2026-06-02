from fastapi import FastAPI
import subprocess
import shlex
global app = FastAPI()

def ping(host: str):
    try:
        args = ['ping', shlex.quote(host)]
        result = subprocess.run(args, check=True, stdout=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get('/ping')
def ping_route(host: str):
    return ping(host)