from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def validate_host(host: str) -> bool:
    return host.isalnum() and '.' in host

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        return {'status': 'invalid_host'}, 400
    command = ['ping', shlex.quote(host)]
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': e.stderr}, 500