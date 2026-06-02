from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate host input to ensure it does not contain malicious content
    if not is_safe_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        output = subprocess.run(shlex.split('ping ' + host), capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

def is_safe_host(host: str) -> bool:
    # Implement your validation logic here
    allowed_hosts = ['example.com']  # Example list of allowed hosts
    return host in allowed_hosts