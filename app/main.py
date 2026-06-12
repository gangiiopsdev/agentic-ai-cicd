from fastapi import FastAPI
import subprocess
def validate_host(host):
    allowed_hosts = ['8.8.8.8', '127.0.0.1']
    return host in allowed_hosts

app = FastAPI()

@app.get("/ping")
def ping(host: str):\n    if not validate_host(host):\n        return {'status': 'failed', 'error': 'Invalid host'}\n    try:\n        output = subprocess.check_output(['ping', '-c', '1', f'{host}'], stderr=subprocess.STDOUT, universal_newlines=True)\n        return {'status': 'completed', 'output': output}\n    except subprocess.CalledProcessError as e:\n        return {'status': 'failed', 'error': e.output}