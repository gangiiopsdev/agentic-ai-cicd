from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    try:
        result = subprocess.run(shlex.split(f'ping -c 1 {shlex.quote(host)}'), capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

def validate_host(host: str):
    allowed_hosts = ['example.com', 'localhost']  # Add allowed hosts here
    if host in allowed_hosts:
        return True
    return False

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        response = safe_ping(host)
        return {'status': 'completed', 'response': response}
    else:
        return {'status': 'error', 'message': 'Host not allowed'}