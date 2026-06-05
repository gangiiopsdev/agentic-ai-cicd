from fastapi import FastAPI
import subprocess
def ping(host: str):
    try:
        # Validate and sanitize host input
        if not all(c.isalnum() or c in '._-:' for c in host):
            raise ValueError('Invalid host name')
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, text=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output}