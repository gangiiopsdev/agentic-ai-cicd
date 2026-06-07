from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(host: str) -> str:
    return ''.join(c for c in host if c.isalnum() or c in ['-', '.', '_'])
def safe_ping(host: str) -> str:
    ping_cmd = ['ping', '-c', '4', shlex.quote(host)]  # Use shlex.quote to safely include user input
    try:
        output = subprocess.check_output(ping_cmd, stderr=subprocess.STDOUT, timeout=10)
        return {'status': 'completed', 'output': output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode('utf-8')}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    return safe_ping(sanitized_host)