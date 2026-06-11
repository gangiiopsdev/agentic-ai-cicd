from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation with shell=False and splitting the command into arguments
    try:
        args = shlex.split(f'ping {host}')
        subprocess.call(args, check=True)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}
    return {'status': 'completed'}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)