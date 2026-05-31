from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str) -> str:
    allowed_hosts = ['example.com', 'test.example.com']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')
    args = ['ping', '-c', '1', host]
    result = subprocess.run(args, capture_output=True, text=True)
    if result.returncode != 0:
        return {'status': 'failed', 'error': result.stderr}
    return {'status': 'completed', 'output': result.stdout}

@app.get('/ping')
def ping(host: str):
    # Validate host input further to ensure it is safe before passing to subprocess
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid host')
    return safe_ping(host)