from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def validate_host(host):
    # Add validation logic here, e.g., allow only specific IP ranges or domain names
    return host.strip() in ['127.0.0.1', '::1']

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    args = ['ping', '-c', '4', shlex.quote(host)]  # Limit the number of pings and quote the host to prevent injection
    try:
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}