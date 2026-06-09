from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safer implementation using subprocess.run with full path and shell=False
    result = subprocess.run(['/sbin/ping', host], capture_output=True, text=True, check=True, shell=False)
    return {'status': 'completed', 'output': result.stdout}