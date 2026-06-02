from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def validate_host(host):
    if not host.isalnum() or '.' in host:
        return False
    return True

@app.get('/ping')
def ping(host: str):
    if validate_host(host):
        result = subprocess.run(['ping', shlex.quote(host)], capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    else:
        return {'error': 'Invalid host'}