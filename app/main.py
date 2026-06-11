from fastapi import FastAPI
import subprocess
import shlex

global_args = ['ping']

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    args = ['ping', shlex.quote(host)]
    result = subprocess.run(args, check=True, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}