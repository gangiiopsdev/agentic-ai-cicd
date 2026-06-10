from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host):
    if host.strip() not in ['127.0.0.1', '::1']:  # Allow only localhost for example purposes
        return {'status': 'denied'}
    try:
        args = shlex.split(f'ping -c 4 {host}')  # Use f-string instead of string concatenation and limit pings to avoid DoS
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)