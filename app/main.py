from fastapi import FastAPI
import subprocess
def is_safe_host(host):
    allowed_hosts = ['example.com', 'test.example.com']
    return host in allowed_hosts

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if is_safe_host(host):
        subprocess.call(['ping', host], shell=False)
        return {'status': 'completed'}
    else:
        return {'status': 'error', 'message': 'Unauthorized host'}, 403

# Fixed code
from fastapi import FastAPI
import subprocess
def is_safe_host(host):
    allowed_hosts = ['example.com', 'test.example.com']
    return host in allowed_hosts

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if is_safe_host(host):
        try:
            result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return {'status': 'completed', 'output': result.stdout.decode()}
        except subprocess.CalledProcessError as e:
            return {'status': 'error', 'message': str(e)}, 500
    else:
        return {'status': 'error', 'message': 'Unauthorized host'}, 403