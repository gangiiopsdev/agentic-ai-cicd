from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Secure implementation with path quoting and shell=False
    try:
        output = subprocess.check_output(shlex.split(f'ping {shlex.quote(host)}'), stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode('utf-8')}

@app.get('/ping')
def ping_endpoint(host: str):
    return ping(host)