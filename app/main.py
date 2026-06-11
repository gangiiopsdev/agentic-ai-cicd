from fastapi import FastAPI
import subprocess
import shlex

def safe_ping(host: str):
    cmd = ['ping', host]
    args = shlex.split(' '.join(cmd))
    subprocess.run(args, check=True)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    safe_ping(host)
    return {'status': 'completed'}