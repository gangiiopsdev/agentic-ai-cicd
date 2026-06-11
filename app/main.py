from fastapi import FastAPI
import subprocess
import shlex

def sanitize_input(input_str):
    return ''.join(e for e in input_str if e.isalnum() or e in ('-', '.'))

def execute_ping(host: str) -> dict:
    try:
        safe_host = sanitize_input(host)
        args = ['ping', shlex.quote(safe_host)]
        subprocess.run(args, check=True, capture_output=True, text=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

app = FastAPI()
@app.get("/ping")
def ping(host: str):
    return execute_ping(host)