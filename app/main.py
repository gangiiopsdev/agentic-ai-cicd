from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_safe_host(host):
    allowed_hosts = ['google.com', 'example.com']
    return host in allowed_hosts

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        return {'error': 'Invalid host'}, 400
    args = ['ping', host]
    subprocess.run(args, check=True)
    return {'status': 'completed'}