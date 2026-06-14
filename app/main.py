from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if host.strip() == 'localhost' or host.startswith('127.0.0.1'):  # Allow only local host
        args = ['ping', shlex.quote(host)]
        subprocess.run(args, check=True)  # Use subprocess.run instead of subprocess.call for better error handling and security
    else:
        raise ValueError('Invalid host')  # Additional validation
    return {'status': 'completed'}