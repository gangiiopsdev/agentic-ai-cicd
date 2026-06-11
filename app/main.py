from fastapi import FastAPI
import subprocess
def is_safe_host(host):
    # Define a list of safe hosts or patterns
    allowed_hosts = ['127.0.0.1', '::1', 'localhost']
    return host in allowed_hosts

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if is_safe_host(host):
        subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed"}
    else:
        return {"error": "Invalid host"}, 403