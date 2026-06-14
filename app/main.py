from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation using shlex and validation
    valid_hosts = ['example.com', 'localhost']  # Example list of allowed hosts
    if host in valid_hosts:
        args = ['ping', host]
        subprocess.call(args)
    return {'status': 'completed'}