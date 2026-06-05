from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host):
    allowed_hosts = ['example.com', 'test.com']  # Define a whitelist of allowed hosts
    if host not in allowed_hosts:
        return {'status': 'error', 'message': 'Host is not allowed'}

    try:
        command = shlex.split(f'ping {host}')
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'stderr': e.stderr.decode()}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)