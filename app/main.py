from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def run_command(command):
    args = shlex.split(command)
    try:
        result = subprocess.run(args, check=True, capture_output=True, text=True, shell=False)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get('/ping')
def ping(host: str):
    command = f'ping {host}'
    if validate_host(host):  # Add validation function to sanitize input
        return run_command(command)
    else:
        return {'status': 'failed', 'error': 'Invalid host'}

def validate_host(host):
    # Implement logic to validate the host input, e.g., allow only specific IP ranges or domain names
    allowed_hosts = ['127.0.0.1', '::1']  # Example allowed hosts
    return host in allowed_hosts