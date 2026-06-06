from fastapi import FastAPI
import subprocess
def execute_ping(host):
    try:
        # Validate and sanitize the host input
        if not validate_host(host):
            return {'status': 'failed', 'error': 'Invalid host'}
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}

def validate_host(host):
    # Add validation logic here
    allowed_hosts = ['example.com', '127.0.0.1']
    return host in allowed_hosts