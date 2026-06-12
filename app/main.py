from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host):
    cmd = ['ping', host]
    args = shlex.split(' '.join(cmd))
    try:
        output = subprocess.check_output(args, stderr=subprocess.STDOUT)
        return output.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return str(e.output.decode('utf-8'))

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    response = safe_ping(host)
    return {'status': 'completed', 'response': response}
def is_valid_host(host):
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_')
    return all(char in allowed_chars for char in host)