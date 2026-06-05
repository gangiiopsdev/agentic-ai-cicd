from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safe implementation using subprocess.run with shell=False and list of arguments
    try:
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'stdout': result.stdout.decode(), 'stderr': result.stderr.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}