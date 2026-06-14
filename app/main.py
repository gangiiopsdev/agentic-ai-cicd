from fastapi import FastAPI
import subprocess
import shlex
def validate_host(host: str):
    allowed_hosts = ['example.com', 'test.com']
    return host in allowed_hosts

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    if not validate_host(host):
        return {'status': 'failed', 'error': 'Host is not allowed'}
    try:
        command = ['ping'] + shlex.split('-c 1 ' + host)
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, text=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e.output)}