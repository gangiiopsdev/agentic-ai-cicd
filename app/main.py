from fastapi import FastAPI
import subprocess
def validate_host(host):
    allowed_hosts = ['example.com', 'localhost']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')
global app
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    # Secure implementation
    validate_host(host)
    subprocess.run(['ping', host], check=True, cwd='/safe/directory')
    return {"status": "completed"}