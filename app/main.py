from fastapi import FastAPI
import subprocess
from os.path import abspath, expandvars
from shlex import quote as cmd_quote

app = FastAPI()

def safe_ping(host):
    try:
        cmd = ['ping', host]
        expanded_cmd = [cmd_quote(cmd_part) for cmd_part in cmd]
        subprocess.run(expanded_cmd, check=True, timeout=5)
        return True
    except subprocess.CalledProcessError as e:
        print(f'Ping failed: {e}')
        return False

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if safe_ping(host):
        return {'status': 'completed', 'result': True}
    else:
        return {'status': 'failed', 'result': False}