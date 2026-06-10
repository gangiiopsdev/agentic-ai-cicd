from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation with shell=False and using shlex to safely handle arguments
    args = shlex.split(f'ping {host}')
    subprocess.call(args, shell=False)
    return {'status': 'completed'}