from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        # Validate and sanitize the input host
        if not is_valid_host(host):
            return {'status': 'failed', 'error': 'Invalid host'}
        command = ['ping', '-c', '1'] + shlex.split(host)
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e.stderr.decode())}

def is_valid_host(host: str) -> bool:
    # Add your validation logic here, e.g., check if the host is in a whitelist
    allowed_hosts = ['example.com', 'localhost']
    return host in allowed_hosts