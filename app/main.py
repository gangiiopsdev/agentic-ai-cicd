from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        args = ['ping', host]
        subprocess.call(shlex.split(' '.join(args)), timeout=5)
        return {'status': 'completed'}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}