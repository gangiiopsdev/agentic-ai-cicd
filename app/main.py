from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation using subprocess.run with shell=False and args= to safely pass arguments.
    result = subprocess.run(['ping', host], capture_output=True, text=True, check=False)
    return {'status': 'completed', 'output': result.stdout}