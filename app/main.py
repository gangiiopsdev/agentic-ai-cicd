from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    # Implement host validation logic here
    allowed_hosts = ['localhost', '127.0.0.1']
    return host in allowed_hosts

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {'status': 'error', 'output': 'Invalid host'}
    try:
        args = ['ping', host]
        result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': e.stderr.decode()}