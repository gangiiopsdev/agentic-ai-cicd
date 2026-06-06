from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    args = ['ping'] + shlex.split(host)
    result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False)
    return {'status': 'completed', 'output': result.stdout.decode(), 'error': result.stderr.decode()}

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)