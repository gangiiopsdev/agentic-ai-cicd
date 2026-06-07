from fastapi import FastAPI
import subprocess
import re
def ping(host: str):
    # Validate hostname
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'status': 'error', 'message': 'Invalid hostname'}

    # Sanitize and escape the input before using it in the subprocess call
    sanitized_host = subprocess.list2cmdline([host])
    args = ['ping', sanitized_host]
    try:
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}