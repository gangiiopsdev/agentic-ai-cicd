from fastapi import FastAPI
import subprocess
import shlex

global_safe_hosts = {'example.com', 'localhost'}

app = FastAPI()

def safe_ping(host: str):
    # Sanitize the host input using shlex.quote
    if host not in global_safe_hosts:
        raise ValueError('Host is not allowed')
    safe_host = shlex.quote(host)
    try:
        result = subprocess.run(['ping', safe_host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed", "output": result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr.decode()}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)