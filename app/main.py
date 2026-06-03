from fastapi import FastAPI
import subprocess
import shlex

def sanitize_input(input_str):
    return ''.join(c for c in input_str if c.isalnum() or c == '.').strip()

def safe_ping(host: str):
    try:
        sanitized_host = sanitize_input(host)
        result = subprocess.run(shlex.split(f'ping {sanitized_host}'), capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(sanitized_host):
        raise ValueError("Invalid host")
    return safe_ping(host)

def is_safe_host(host: str):
    allowed_hosts = ['localhost', '127.0.0.1']
    return host in allowed_hosts