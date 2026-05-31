from fastapi import FastAPI
import subprocess
def ping(host: str):
    try:
        # Secure implementation using subprocess.run with shell=False and validated input
        if all(char.isalnum() or char in '-.' for char in host):
            result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        else:
            raise ValueError('Invalid input')
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}