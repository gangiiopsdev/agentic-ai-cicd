from fastapi import FastAPI
import subprocess
import shlex
def is_valid_ip(ip):
    parts = ip.split('.')
    return len(parts) == 4 and all(part.isdigit() and 0 <= int(part) <= 255 for part in parts)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not is_valid_ip(host):
        return {'error': 'Invalid host address'}
    try:
        result = subprocess.run(shlex.split(f'ping -c 1 {host}'), capture_output=True, text=True, timeout=5)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.TimeoutExpired:
        return {'status': 'timeout', 'output': 'Ping operation timed out.'}