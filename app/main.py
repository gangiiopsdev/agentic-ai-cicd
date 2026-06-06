from fastapi import FastAPI
import subprocess
import shlex
import shlex

app = FastAPI()

def is_valid_host(host):
    return host.isdigit()

@app.get('/ping')
def ping(host: str):
    if is_valid_host(host):
        command = ['ping', host]
        args = shlex.split(' '.join(command))
        result = subprocess.run(args, capture_output=True, text=True, check=False)
        return {'status': 'completed', 'output': result.stdout}
    else:
        return {'error': 'Invalid host'}, 400