from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def secure_ping(host: str):
    if not host.startswith('192.168.') or not host.replace('.', '', 3).isdigit():
        return {'status': 'invalid_host'}
    ping_command = ['ping', shlex.quote(host)]
    try:
        subprocess.run(ping_command, shell=False, check=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping(host: str):
    return secure_ping(host)