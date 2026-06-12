from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Safe implementation using subprocess.run with shell=False and list of arguments, escaping user input
    args = shlex.split(f'ping {host}')
    subprocess.run(args, check=True)
    return {'status': 'completed'}