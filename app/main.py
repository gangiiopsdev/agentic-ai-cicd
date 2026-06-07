from fastapi import FastAPI
import subprocess
import shlex
def ping(host: str):
    try:
        # Validate the host input to ensure it does not contain malicious content
        if not is_valid_host(host):
            raise ValueError('Invalid host')
        command = ['ping', host]
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=False)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}
def is_valid_host(host: str) -> bool:
    # Implement validation logic here
    return host.isalnum() and '.' in host