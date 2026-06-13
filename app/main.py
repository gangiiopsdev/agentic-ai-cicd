from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_subprocess(cmd, args):
    try:
        output = subprocess.check_output([' '.join(cmd) + ' ' + ' '.join(args)], stderr=subprocess.STDOUT)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}

@app.get('/ping')
def ping(host: str):
    cmd = ['ping']
    args = [host]
    return safe_subprocess(cmd, args)