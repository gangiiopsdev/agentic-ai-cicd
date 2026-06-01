from fastapi import FastAPI
import subprocess

def ping(host: str):
    try:
        # Secure implementation using subprocess.run with shell=False and validated input
        allowed_chars = set(char.isalnum() or char in '-.' for char in host)
        if all(allowed_chars):
            result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        else:
            raise ValueError('Invalid input')
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}