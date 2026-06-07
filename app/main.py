from fastapi import FastAPI
import subprocess
def safe_ping(host):
    allowed_hosts = ['127.0.0.1', 'localhost']
    if host in allowed_hosts:
        try:
            result = subprocess.run(['ping', '-c', '4', host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}
    else:
        return {'status': 'failed', 'error': 'Unsafe host'}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not host:
        return {'status': 'failed', 'error': 'Host parameter is missing'}
    # Use a whitelist of allowed hosts instead of checking for disallowed ones
    allowed_hosts = ['127.0.0.1', 'localhost']
    if host in allowed_hosts:
        try:
            result = subprocess.run(['ping', '-c', '4', host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}
    else:
        return {'status': 'failed', 'error': 'Unsafe host'}