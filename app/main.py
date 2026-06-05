from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def run_safe_ping(host: str):
    # Define allowed hosts or use whitelist/blacklist approach
    allowed_hosts = ['google.com', 'example.com']
    if host not in allowed_hosts:
        return {'status': 'error', 'message': 'Host not allowed'}

    args = shlex.split(f'ping {host}')
    try:
        subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}

@app.get('/ping')
def ping(host: str):
    return run_safe_ping(host)