from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    args = ['ping'] + shlex.split(host)
    result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout, 'error': result.stderr}

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)