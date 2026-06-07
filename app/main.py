from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_safe_host(host):
    allowed_hosts = ['example.com', 'test.com']
    return host in allowed_hosts

@app.get("/ping")
def ping(host: str):
    if is_safe_host(host):
        # Use a whitelist of allowed commands and arguments
        subprocess.call(['ping'], shell=False)
        return {'status': 'completed'}
    else:
        return {'error': 'Invalid host'}, 403