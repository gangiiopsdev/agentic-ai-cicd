from fastapi import FastAPI
import subprocess
from shlex import quote
def safe_ping(host):
    try:
        output = subprocess.check_output(['ping', '-c 1', quote(host)], stderr=subprocess.STDOUT, shell=False)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)