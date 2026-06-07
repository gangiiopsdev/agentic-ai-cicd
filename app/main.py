from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def run_safe_command(command_parts):
    try:
        result = subprocess.run(command_parts, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    allowed_hosts = ['8.8.8.8', '127.0.0.1']  # Example allowed hosts
    if host in allowed_hosts:
        command_parts = shlex.split('ping -c 4 ' + shlex.quote(host))
        return run_safe_command(command_parts)
    else:
        return {'status': 'invalid host', 'error': 'Host not allowed'}