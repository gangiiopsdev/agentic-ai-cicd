from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    allowed_hosts = ['example.com']  # Define allowed hosts
    if host in allowed_hosts:
        try:
            output = subprocess.check_output(['ping', '-c', '1', host], stderr=subprocess.STDOUT, text=True)
            return {'status': 'completed', 'output': output}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.output}
    else:
        return {'status': 'failed', 'error': 'Host not allowed'}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate the host against a whitelist to mitigate some risks
    if '@' in host or '\' in host:
        return {'status': 'failed', 'error': 'Invalid host format'}
    return safe_ping(host)