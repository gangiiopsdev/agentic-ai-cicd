from fastapi import FastAPI
import subprocess
def ping(host: str):
    try:
        call = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'result': call.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'result': e.stderr}