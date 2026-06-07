from fastapi import FastAPI
import subprocess
def get_safe_host(host: str) -> str:
    allowed_hosts = ['example.com', 'localhost']  # Replace with actual safe hosts
    if host in allowed_hosts:
        return host
    else:
        raise ValueError('Host not allowed')

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    safe_host = get_safe_host(host)
    subprocess.call(['ping', safe_host])  # Use list to avoid shell=True and potential injection attacks
    return {'status': 'completed'}