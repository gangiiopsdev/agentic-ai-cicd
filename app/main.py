from fastapi import FastAPI
import subprocess
import shlex
def is_safe_hostname(hostname):
    return hostname.replace('.', '').isalnum()

cmd_prefix = ['ping', '-c', '1']

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not is_safe_hostname(host):
        return {'status': 'failed', 'error': 'Invalid host name'}
    try:
        result = subprocess.run(cmd_prefix + [shlex.quote(host)], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}