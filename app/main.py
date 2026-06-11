from fastapi import FastAPI
import subprocess
from shlex import quote as shell_quote

app = FastAPI()

def sanitize_host(host: str) -> bool:
    return host.isalnum()

@app.get('/ping')
def ping(host: str):
    if not sanitize_host(host):
        return {'status': 'error', 'message': 'Invalid hostname'}
    try:
        command = [shell_quote('ping'), shell_quote(host)]
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'stderr': e.stderr.decode()}