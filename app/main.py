from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def secure_ping(host):
    try:
        args = ['ping', '-c', '1'] + shlex.split(host)
        result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}

@app.get("/ping")
def ping(host: str):
    if not host.isalnum():  # Simple input validation
        return {'status': 'failed', 'error': 'Invalid host'}
    return secure_ping(host)