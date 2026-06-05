from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    if not host.isdigit():
        return {'status': 'failed', 'error': 'Invalid input'}
    args = shlex.split('ping ' + host)
    result = subprocess.run(args, capture_output=True, text=True, check=False)
    if result.returncode != 0:
        return {'status': 'failed', 'error': result.stderr}
    return {'status': 'completed', 'output': result.stdout}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)