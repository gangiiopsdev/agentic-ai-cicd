from fastapi import FastAPI
import subprocess
def ping(host: str):
    try:
        # Validate the host parameter to ensure it only contains allowed characters
        if not host.isalnum() and '-' not in host:
            raise ValueError('Invalid host parameter')
        subprocess.call(['ping', '-c', '1', host])
        return {'status': 'completed'}
    except Exception as e:
        return {'error': str(e)}, 500