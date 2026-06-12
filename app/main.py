from fastapi import FastAPI
import subprocess
import shlex
def escape_shell_arg(s):
    return ' '.join(shlex.quote(arg) for arg in s.split())

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    safe_host = escape_shell_arg(host)
    try:
        subprocess.run(['ping', safe_host], check=True, text=True, capture_output=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}