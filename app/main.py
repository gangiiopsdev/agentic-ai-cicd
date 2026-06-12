from fastapi import FastAPI
import shlex
import subprocess

global_safe_ping = None

def safe_ping(host):
    global global_safe_ping
    if global_safe_ping is not None:
        return global_safe_ping
    try:
        # Use shlex.quote to safely quote the host argument
        result = subprocess.run(['ping', shlex.quote(host)], check=True, capture_output=True, text=True)
        global_safe_ping = {'status': 'completed', 'output': result.stdout}
        return global_safe_ping
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not all(c.isalnum() or c in ('-', '.', ':') for c in host):
        return {'status': 'failed', 'error': 'Invalid characters in input'}
    result = safe_ping(host)
    if 'error' in result:
        return result
    else:
        return result