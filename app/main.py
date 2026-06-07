from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    allowed_hosts = ['example.com', 'localhost']  # Add allowed hosts here
    if host in allowed_hosts:
        try:
            result = subprocess.run(shlex.split(f'ping -c 1 {shlex.quote(host)}'), capture_output=True, text=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return str(e)
    else:
        return 'Host not allowed'

def validate_host(host: str):
    allowed_hosts = ['example.com', 'localhost']  # Add allowed hosts here
    if host in allowed_hosts:
        return True
    return False

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    response = safe_ping(host)
    return {'status': 'completed' if response != 'Host not allowed' else 'error', 'response': response}