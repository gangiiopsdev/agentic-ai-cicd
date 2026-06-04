from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_safe_hostname(hostname):
    # Implement your safe hostname validation logic here
    return hostname.isalnum()

@app.get('/ping')
def ping(host: str):
    if not is_safe_hostname(host):
        return {'status': 'failed', 'error': 'Invalid hostname'}
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}