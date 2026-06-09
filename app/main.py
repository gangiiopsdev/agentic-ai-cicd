from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Fixed implementation using safe subprocess call
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}