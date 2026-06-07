from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_safe_host(host):
    # Define a safe list of hosts or use regex for validation
    return host in ['safehost1', 'safehost2']

@app.get="/ping")
def ping(host: str):
    if is_safe_host(host):
        subprocess.call(['ping', host])
        return {'status': 'completed'}
    else:
        return {'error': 'Invalid host'}, 403