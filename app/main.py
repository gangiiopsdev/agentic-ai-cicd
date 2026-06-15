from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host):
    try:
        result = subprocess.run(['ping', '-c', '1', f'-{shlex.quote(host)}'], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e.stderr)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not host.isalnum():
        return {'status': 'failed', 'error': 'Invalid host name'}
    # Validate the host further to ensure it's safe to use with subprocess
    allowed_hosts = ['example.com', 'localhost']
    if host in allowed_hosts:
        return safe_ping(host)
    else:
        return {'status': 'failed', 'error': 'Host not allowed'}