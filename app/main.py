from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    allowed_hosts = ['example.com']  # Define a whitelist of allowed hosts
    if host in allowed_hosts:
        try:
            args = ["ping", host]
            output = subprocess.check_output(args, stderr=subprocess.STDOUT, shell=False)
            return {'status': 'completed', 'output': output.decode('utf-8')}
        except subprocess.CalledProcessError as e:
            return {'status': 'error', 'output': e.output.decode('utf-8')}
    else:
        return {'status': 'error', 'output': 'Host not allowed'}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)