from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize the host input
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        output = subprocess.check_output(['ping', '-c', '1', host], stderr=subprocess.STDOUT, text=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

# Additional mitigation: Use a whitelist for allowed hosts
allowed_hosts = ['example.com', 'test.com']
def ping(host: str):
    if host not in allowed_hosts:
        return {'status': 'failed', 'error': 'Host not allowed'}
    # Validate and sanitize the host input
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        output = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

# Use a context manager to ensure the process is terminated if an exception occurs
with subprocess.Popen(['ping', '-c', '1', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE) as ping_process:
    output, error = ping_process.communicate()
    return_code = ping_process.returncode
    if return_code == 0:
        return {'status': 'completed', 'output': output.decode('utf-8')}
    else:
        return {'status': 'failed', 'error': error.decode('utf-8')}