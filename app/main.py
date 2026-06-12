from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation with input validation
    allowed_hosts = ['8.8.8.8', '127.0.0.1']  # Example allowed hosts
    if host in allowed_hosts:
        args = ['ping', host]
        subprocess.call(args, shell=False)  # Use shell=False to avoid shell injection
        return {'status': 'completed'}
    else:
        return {'status': 'invalid_host', 'message': 'Host not allowed'}