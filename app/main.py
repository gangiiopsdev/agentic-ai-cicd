from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation using subprocess.run with shell=False and proper argument handling
    if host.strip() == 'localhost' or host.strip() == '127.0.0.1':
        args = ['ping', host]
        result = subprocess.run(args, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    else:
        return {'status': 'error', 'message': 'Invalid host'}