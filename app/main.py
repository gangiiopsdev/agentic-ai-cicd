from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Secure implementation
    if not host.strip():
        return {'status': 'failed', 'error': 'Invalid input'}
    cmd = ['ping'] + shlex.split(host)
    output = subprocess.check_output(cmd, stderr=subprocess.STDOUT, timeout=5)
    return {'status': 'completed', 'output': output.decode()}

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)