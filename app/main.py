from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    try:
        cmd = ['ping', host]
        args = shlex.split(' '.join(cmd))
        output = subprocess.check_output(args, stderr=subprocess.STDOUT, text=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.__repr__()}

@app.get('/ping')
def ping_wrapper(host: str):
    return ping(host)