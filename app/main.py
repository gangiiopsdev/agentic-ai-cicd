from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

allowed_hosts = ['example.com', 'another-example.com']  # Define allowed hosts

def safe_ping(host: str):
    if host in allowed_hosts and re.match(r'^[a-zA-Z0-9.-]+$', host):
        args = ['ping', shlex.quote(host)]
        result = subprocess.run(args, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    else:
        return {'status': 'failed', 'message': 'Host not allowed'}

@app.get("/ping")
def ping(host: str):
    if re.match(r'^[a-zA-Z0-9.-]+$', host) and host in allowed_hosts:
        return safe_ping(host)
    else:
        return {'status': 'failed', 'message': 'Invalid or unauthorized host'}