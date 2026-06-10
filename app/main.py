from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    try:
        cmd = ['ping', host]
        args = shlex.split(' '.join(cmd))
        output = subprocess.check_output(args, stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode('utf-8')}

@app.get("/ping")
def ping(host: str):
    if host.startswith('.') or '@' in host:
        return {'status': 'failed', 'error': 'Invalid input'}
    return safe_ping(host)