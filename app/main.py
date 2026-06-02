from fastapi import FastAPI
import subprocess
import shlex
def validate_host(host: str) -> bool:
    ALLOWED_HOSTS = ['example.com', 'test.com']
    return host in ALLOWED_HOSTS

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        return {'status': 'failed', 'error': 'Host is not allowed'}
    try:
        args = shlex.split('ping ' + host)
        result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}