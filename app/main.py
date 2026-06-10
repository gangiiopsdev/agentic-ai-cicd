from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def run_ping(host):
    try:
        command = ['ping', shlex.quote(host)]
        result = subprocess.run(command, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        return {'status': 'invalid host'}
    return run_ping(host)

def is_valid_host(host):
    # Simple validation to allow only alphanumeric characters and hyphens
    import re
    pattern = re.compile(r'^[a-zA-Z0-9-]+$')
    return bool(pattern.match(host))