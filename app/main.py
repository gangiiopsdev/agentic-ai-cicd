from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    try:
        output = subprocess.check_output(shlex.split('ping ' + host), stderr=subprocess.STDOUT, shell=False)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}

@app.get("/ping")
def ping(host: str):
    if not host or len(host) > 255 or any(char in host for char in '"`$&*;{}[]|\^~<>?#\\'):
        return {'status': 'failed', 'error': 'Invalid input'}
    return safe_ping(host)