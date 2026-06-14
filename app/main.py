from fastapi import FastAPI
import subprocess
import shlex
def ping(host: str):
    # Secure implementation
    try:
        output = subprocess.check_output(shlex.split('ping ' + host), stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}

app = FastAPI()

@app.get("/ping")
def ping_route(host: str):
    return ping(host)