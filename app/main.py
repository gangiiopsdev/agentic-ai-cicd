from fastapi import FastAPI
import subprocess
def ping(host: str):
    try:
        # Validate the host input
        if not host.isalnum():
            raise ValueError('Invalid host name')
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}
    except ValueError as ve:
        return {'status': 'failed', 'error': str(ve)}