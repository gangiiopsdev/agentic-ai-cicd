from fastapi import FastAPI
import subprocess
def ping(host: str):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True, cwd='/bin/')
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}