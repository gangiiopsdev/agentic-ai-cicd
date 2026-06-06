from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    allowed_hosts = ['example.com']  # Define allowed hosts
    if host in allowed_hosts:
        try:
            args = ["ping", "-c", "1", shlex.quote(host)]
            output = subprocess.run(args, capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': output.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.stderr}
    else:
        return {'status': 'failed', 'error': 'Host not allowed'}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)