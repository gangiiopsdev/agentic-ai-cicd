from fastapi import FastAPI
import subprocess
def validate_host(host):
    allowed_hosts = ['8.8.8.8', '127.0.0.1']
    return host in allowed_hosts

def sanitize_input(input_string):
    return ''.join(c for c in input_string if c.isdigit() or c == '.').strip()

app = FastAPI()

@app.get("/ping")
def ping(host: str):\n    sanitized_host = sanitize_input(host)
    if not validate_host(sanitized_host):\n        return {'status': 'failed', 'error': 'Invalid host'}\n    try:\n        output = subprocess.check_output(['ping', '-c', '1', f'{sanitized_host}'], stderr=subprocess.STDOUT, universal_newlines=True)\n        return {'status': 'completed', 'output': output}\n    except subprocess.CalledProcessError as e:\n        return {'status': 'failed', 'error': e.output}