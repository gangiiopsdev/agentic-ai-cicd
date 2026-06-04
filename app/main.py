from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(user_input):
    safe_input = ''.join(c for c in user_input if c.isalnum() or c in ('.', '-', '_'))
    return safe_input

@app.get('/ping')
def ping(host: str):
    try:
        safe_host = sanitize_input(host)
        output = subprocess.check_output(['ping', '-c 1', safe_host], stderr=subprocess.STDOUT, timeout=5, shell=False)
        return {'status': 'completed', 'output': output.decode('utf-8')}
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as e:
        return {'status': 'failed', 'error': str(e)}