from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Fixed implementation with explicit shell=True for safety
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True, shell=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}