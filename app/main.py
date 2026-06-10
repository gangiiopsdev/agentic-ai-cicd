from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    # Define a whitelist of allowed hosts
    allowed_hosts = ['example.com', 'localhost']
    if host not in allowed_hosts:
        raise ValueError('Unauthorized host')

    try:
        args = shlex.split(f'ping -c 4 {host}')
        result = subprocess.run(args, check=True, capture_output=True)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}

@app.get("/ping")
def ping(host: str):
    try:
        safe_ping(host)
    except ValueError as e:
        return {'status': 'error', 'message': str(e)}
    return {'status': 'completed'}