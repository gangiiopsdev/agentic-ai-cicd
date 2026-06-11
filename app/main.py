from fastapi import FastAPI
import subprocess
import shlex
class SafeSubprocess:
    @staticmethod
def ping(host: str):
        # Use a secure validation method instead of a hardcoded whitelist
        if not validate_host(host):
            return {'error': 'Invalid input'}
        command = ['ping', shlex.quote(host)]  # Use shlex.quote to safely quote the host
        try:
            result = subprocess.run(command, check=True, capture_output=True, text=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'error': e.stderr}

def validate_host(host: str):
    # Implement a secure validation method here
    allowed_hosts = ['example.com', 'test.com']  # Replace with actual list of allowed hosts
    return host in allowed_hosts

global_app = FastAPI()

@app.get("/ping")
def ping_safe(host: str):
    return SafeSubprocess.ping(host)