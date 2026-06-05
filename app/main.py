from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def is_valid_host(host):
    # Add validation logic here
    return host.isdigit()

@app.get('/ping')
def ping(host: str):
    if is_valid_host(host):
        command = ['ping', host]
        args = shlex.split(' '.join(command))
        subprocess.run(args, check=True)
        return {'status': 'completed'}
    else:
        return {'error': 'Invalid host'}, 400