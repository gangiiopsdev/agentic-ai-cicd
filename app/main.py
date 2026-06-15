from fastapi import FastAPI
import subprocess
import shlex
def ping(host: str):
    try:
        command = ['ping', host]
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, text=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output}

app = FastAPI()

@app.get('/ping')
def ping_wrapper(host: str):
    return ping(host)