from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Safe implementation
    try:
        args = shlex.split(f'ping {host}')
        output = subprocess.check_output(args, stderr=subprocess.STDOUT)
        return {'status': 'completed', 'output': output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode('utf-8')}