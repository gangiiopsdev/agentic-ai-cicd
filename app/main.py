from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def is_safe_host(host):
    # Implement logic to validate host (e.g., allow only specific hosts)
    allowed_hosts = ['example.com', 'test.com']
    return host in allowed_hosts

@app.get('/ping')
def ping(host: str):
    if not is_safe_host(host):
        raise ValueError('Invalid host')
    cmd = ['ping', shlex.quote(host)]
    result = subprocess.run(cmd, check=True, capture_output=True)
    return {'status': 'completed', 'output': result.stdout.decode()}