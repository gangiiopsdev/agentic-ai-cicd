from fastapi import FastAPI
import subprocess
import shlex

global app = FastAPI()

def safe_ping(host):
    args = ['ping', *shlex.split(host)]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

@app.get('/ping')
def ping(host: str):
    response = safe_ping(host)
    return {'status': 'completed', 'response': response}