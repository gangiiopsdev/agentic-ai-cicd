from fastapi import FastAPI
import subprocess
import shlex

global_args = shlex.split('ping')

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    args = global_args + [shlex.quote(host)]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}