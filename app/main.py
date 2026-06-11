from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        # Validate and sanitize the host input
        if not validate_host(host):
            raise ValueError('Invalid host input')
        command = ['ping', '-c 1', shlex.quote(host)]  # Use shlex.quote to safely quote the argument
        output = subprocess.run(command, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

def validate_host(host: str) -> bool:
    # Implement validation logic for host input
    allowed_hosts = ['example.com', 'test.com']  # Example list of allowed hosts
    return host in allowed_hosts