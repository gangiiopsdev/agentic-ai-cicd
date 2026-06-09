from fastapi import FastAPI
import subprocess
def ping(host: str):
    try:
        # Use check_output instead of call for better error handling and security
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode('utf-8')}