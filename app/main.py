from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping_safe(host: str):
    try:
        args = shlex.split(f'ping {host}')
        result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}

@app.get("/ping")
def ping(host: str):
    return ping_safe(host)