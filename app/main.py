from fastapi import FastAPI
import subprocess
def is_safe_host(host):
    allowed_hosts = ['127.0.0.1', '::1']
    return host in allowed_hosts
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    if is_safe_host(host):
        # Secure implementation using subprocess.run with shell=False and args parameter
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    else:
        return {"status": "error", "message": "Invalid host"}