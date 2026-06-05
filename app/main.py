from fastapi import FastAPI
import subprocess

def ping(host: str):
    try:
        # Sanitize the host input
        safe_host = host.strip()
        output = subprocess.check_output(['ping', safe_host], stderr=subprocess.STDOUT)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}