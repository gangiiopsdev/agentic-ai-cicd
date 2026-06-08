from fastapi import FastAPI
import shlex
import subprocess

def safe_ping(host):
    cmd = ['ping', host]
    args = shlex.split(' '.join(cmd))
    try:
        result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e.stderr)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)