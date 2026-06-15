from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host):
    try:
        cmd = ['ping'] + shlex.split(host)
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT, timeout=5)
        return output.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return e.output.decode('utf-8')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if 'ping' not in host:
        return {'status': 'error', 'result': 'Invalid input'}
    result = safe_ping(host)
    return {'status': 'completed', 'result': result}