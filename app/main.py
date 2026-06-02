from fastapi import FastAPI
import subprocess

def ping(host: str):
    try:
        # Validate and sanitize host input
        if not is_valid_host(host):
            return {'status': 'failed', 'error': 'Invalid host'}
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

# Example validation function (simplified)
def is_valid_host(host: str) -> bool:
    # Add your validation logic here, e.g., check for valid IP addresses or hostnames
    return True