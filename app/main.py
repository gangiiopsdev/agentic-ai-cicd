from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_safe_host(host):
    allowed_hosts = ['example.com', 'localhost']
    return host in allowed_hosts

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        return {'error': 'Invalid host'}, 403

    # Safe implementation
    subprocess.call(['ping', host])

    return {'status': 'completed'}