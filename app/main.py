from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def _ping(host: str):
    try:
        args = shlex.split('ping ' + host)
        subprocess.run(args, check=True, timeout=5)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get('/ping')
def ping(host: str):
    return _ping(host)