from fastapi import FastAPI
import subprocess
def ping(host: str):
    try:
        # Using check_output instead of call for better error handling and no shell=True
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}