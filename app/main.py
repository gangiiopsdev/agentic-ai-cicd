from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    if not host.isalnum():
        return {'status': 'error', 'message': 'Invalid host name'}
    try:
        output = subprocess.check_output(['ping'] + shlex.split(host), timeout=5, stderr=subprocess.STDOUT)
        return {'status': 'completed', 'output': output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': e.output.decode('utf-8')}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)