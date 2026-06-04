from fastapi import FastAPI
import subprocess
from subprocess import Popen, PIPE

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        process = Popen(['ping', host], stdout=PIPE, stderr=PIPE, timeout=5)
        output, error = process.communicate()
        if process.returncode != 0:
            return {'status': 'failed', 'error': error.decode('utf-8')}
        else:
            return {'status': 'completed', 'output': output.decode('utf-8')}
    except subprocess.TimeoutExpired as e:
        return {'status': 'failed', 'error': str(e)}