from fastapi import FastAPI
import subprocess
def ping(host: str):
    try:
        # Validate the host to ensure it's a valid IP or hostname
        if not (host.strip() and all(c.isalnum() or c in '.-' for c in host)):
            raise ValueError('Invalid host format')
        output = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True, shell=False)
        return {'status': 'completed', 'output': output.stdout}
    except (subprocess.CalledProcessError, ValueError) as e:
        return {'status': 'failed', 'error': str(e)}