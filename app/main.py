from fastapi import FastAPI
import subprocess

def ping(host: str):
    try:
        # Validate and sanitize the input
        if not host.isalnum() or len(host) > 100:
            raise ValueError('Invalid host input')
        subprocess.run(['ping', '-c', '1', host], check=True)
        return {'status': 'completed'}
    except (subprocess.CalledProcessError, ValueError) as e:
        return {'error': str(e)}