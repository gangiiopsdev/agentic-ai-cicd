from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    # Sanitize input to prevent injection
    allowed_hosts = ['127.0.0.1', '::1']  # Example allowed hosts
    if host not in allowed_hosts:
        raise ValueError('Host not allowed')
    args = ['ping'] + shlex.split(host)
    try:
        result = subprocess.run(args, check=True, capture_output=True, text=True, shell=False)  # Add shell=False to avoid command injection
        return result.stdout
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    response = safe_ping(host)
    if isinstance(response, dict) and 'status' in response and response['status'] == 'error':
        return response
    else:
        return {'status': 'completed', 'output': response}