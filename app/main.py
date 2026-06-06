from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_valid_host(host):
    # Simple whitelist example; replace with more comprehensive validation
    allowed_hosts = ['example.com', 'localhost']
    return host in allowed_hosts

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        raise ValueError('Invalid host')
    args = ['ping', host]
    subprocess.run(args, check=True)
    return {"status": "completed"}