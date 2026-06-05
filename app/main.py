from fastapi import FastAPI
import subprocess
import shlex
class SafeHostValidator:
    @staticmethod
def safe_host(host):
        return host.isalnum() and len(host) <= 100

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not SafeHostValidator.safe_host(host):
        return {'status': 'error', 'message': 'Invalid input'}
    try:
        result = subprocess.run(['ping', shlex.quote(host)], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': e.stderr}