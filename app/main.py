from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def validate_host(host):
    # Add validation logic here, e.g., allow only specific IP ranges or domain names
    return host.strip() in ['127.0.0.1', '::1']

@app.get('/ping')
def ping(host: str):\n    if not validate_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}\n    args = ['ping'] + shlex.split(host)
    try:
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:\n        return {'status': 'failed', 'error': str(e)}