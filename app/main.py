from fastapi import FastAPI
import subprocess
def safe_ping(host: str) -> bool:
    allowed_hosts = ['127.0.0.1', 'localhost']  # Define a whitelist of allowed hosts
    if host in allowed_hosts and re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', host):
        subprocess.call(['ping', host])
        return True
    else:
        return False

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if safe_ping(host):
        return {"status": "completed"}
    else:
        return {"status": "error", "message": "Invalid host"}