from fastapi import FastAPI
import subprocess
import shlex
global_args = ['ping', shlex.quote(host)]

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        result = subprocess.run(global_args, check=True)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e.stderr)}