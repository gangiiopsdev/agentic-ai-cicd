from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def is_safe_hostname(hostname):
    return all(c.isalnum() or c in '._-' for c in hostname)

def safe_ping(host):
    command = ['ping', shlex.quote(host)]  # Use shlex.quote to safely quote the user input
    result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {'status': 'completed', 'output': result.stdout.decode()}

@app.get("/ping")
def ping(host: str):
    if not is_safe_hostname(host):
        return {'status': 'failed', 'error': 'Invalid hostname'}
    try:
        return safe_ping(host)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}