from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize the host input
    if not validate_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        args = shlex.split(f'ping {host}')
        output = subprocess.run(args, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

def validate_host(host: str) -> bool:
    # Implement input validation logic here
    allowed_hosts = ['example.com', 'localhost']  # Example list of allowed hosts
    return host in allowed_hosts