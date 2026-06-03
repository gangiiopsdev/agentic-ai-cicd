from fastapi import FastAPI
import subprocess
def ping(host: str):
    try:
        # Use check_output to avoid shell=True and prevent injection
        result = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'result': result.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}