from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def validate_host(host: str) -> bool:
    return host.isalnum()

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        raise ValueError("Invalid host")
    try:
        args = shlex.split('ping ' + host)
        output = subprocess.check_output(args, shell=False, timeout=5)
        return {'status': 'completed', 'output': output.decode()}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}