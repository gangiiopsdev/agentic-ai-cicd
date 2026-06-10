from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    args = ['ping'] + [shlex.quote(arg) for arg in host.split()]
    result = subprocess.run(args, capture_output=True, text=True, check=False)
    return result.stdout

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    response = safe_ping(shlex.quote(host))
    return {'status': 'completed', 'output': response}