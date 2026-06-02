from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_safe_host(host):
    # Add logic to check if host is safe, e.g., whitelist specific domains/IPs
    return True

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        return {'status': 'failed', 'error': 'Unsafe host'}
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT)
        return {'status': 'completed', 'output': output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode('utf-8')}