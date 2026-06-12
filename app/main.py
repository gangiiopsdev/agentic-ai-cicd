from fastapi import FastAPI
import subprocess
def validate_host(host):
    allowed_hosts = ['127.0.0.1', '::1']
    return host in allowed_hosts

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if validate_host(host) and host.replace('.', '', 3).isdigit() or ':' in host:
        # Use shell=False to avoid command injection
        subprocess.run(['ping', host], check=True, shell=False)
        return {"status": "completed"}
    else:
        return {"error": "Invalid host"}, 400