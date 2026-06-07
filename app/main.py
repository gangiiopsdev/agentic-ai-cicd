from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_safe_host(host):
    # Define a list of allowed hosts or implement more complex validation logic
    return host in ['example.com', 'test.com']

@app.get('/ping')
def ping(host: str):
    if not is_safe_host(host):
        return {'status': 'error', 'message': 'Host is not allowed'}
    # Fixed implementation using subprocess.run with shell=False and additional validation
    result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
    try:
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}