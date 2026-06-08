from fastapi import FastAPI
import subprocess
import shlex

global app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        host = shlex.quote(host)
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, text=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output}