from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Input validation with sanitization
    if not host.strip():
        raise ValueError('Host parameter is required')
    try:
        args = ['ping'] + shlex.split(host)
        subprocess.run(args, check=True, shell=False)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

    return {'status': 'completed'}