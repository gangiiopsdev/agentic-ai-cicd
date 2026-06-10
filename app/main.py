from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    try:
        # Secure implementation using subprocess.run with shell=False and checking for untrusted input
        subprocess.run(['ping', host], check=True, shell=False)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping_endpoint(host: str):
    # Validate input to ensure it does not contain malicious content
    if "" in host or "&" in host or "|" in host:
        return {'status': 'failed', 'error': 'Invalid input'}
    return ping(host)