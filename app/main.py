from fastapi import FastAPI
import subprocess
import shlex
def secure_ping(host):
    try:
        args = ['ping', '-c', '1'] + shlex.split(shlex.quote(host))
        result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Enhanced input validation to include more characters
    if not host.isalnum() and not host.replace('-', '').replace('.', '').isalnum():
        return {'status': 'failed', 'error': 'Invalid host'}
    return secure_ping(host)