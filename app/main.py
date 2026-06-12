from fastapi import FastAPI
import subprocess
def is_safe_host(host):
    return host.isalnum() and len(host) <= 15
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        raise ValueError('Invalid host name')
    try:
        subprocess.run(['ping', '-c', '1', host], check=True, shell=False)
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}
    return {"status": "completed"}