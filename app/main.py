from fastapi import FastAPI
import subprocess
import shlex
def safe_host(host):
    # Validate and sanitize the host input to prevent command injection
    allowed_hosts = ['example.com', 'localhost']  # Define a list of allowed hosts
    if host in allowed_hosts:
        return True
    return False
app = FastAPI()
@app.get('/ping')
def ping(host: str):
    if safe_host(host):
        # Secure implementation with absolute path and argument handling
        result = subprocess.run(['/usr/bin/ping', '-c 1'] + shlex.split(shlex.quote(host)), capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    else:
        return {'status': 'error', 'message': 'Host not allowed'}