from fastapi import FastAPI
import subprocess
import shlex
def ping(host: str):
    try:
        # Safe implementation using subprocess.run with shell=False and shlex.split for safe command construction
        result = subprocess.run(shlex.split('ping ' + host), check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)