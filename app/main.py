from fastapi import FastAPI
import subprocess

def ping(host: str):
    try:
        # Validate and sanitize the host input
        if not host.isdigit() or len(host) > 15:
            raise ValueError("Invalid host")
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}
    except ValueError as ve:
        return {'status': 'failed', 'error': str(ve)}