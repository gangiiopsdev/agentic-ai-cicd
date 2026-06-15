from fastapi import FastAPI
import subprocess
import shlex
def is_safe_hostname(hostname):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return all(char in allowed_chars for char in hostname)
def execute_ping(host):
    try:
        command = f'ping -c 1 {shlex.quote(host)}'
        result = subprocess.run(command, capture_output=True, text=True, check=True, shell=False)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': e.stderr}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not is_safe_hostname(host):
        return {'status': 'error', 'message': 'Invalid host name'}
    return execute_ping(host)