from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input_str):
    return ''.join(ch for ch in input_str if ch.isalnum() or ch in ('.', '-', '_'))

@app.get('/ping')
def ping(host: str):
    safe_host = sanitize_input(host)
    try:
        subprocess.run(['ping', shlex.quote(safe_host)], check=True, timeout=5)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}
    return {'status': 'completed'}