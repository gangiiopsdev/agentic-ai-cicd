from fastapi import FastAPI
import subprocess
global allow_ping = False
def check_host(host):
    allowed_hosts = ['127.0.0.1', '::1']  # Add more allowed hosts as needed
    if host in allowed_hosts:
        return True
    return False
app = FastAPI()
@app.get("/ping")
def ping(host: str):    if check_host(host):
        subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True)
        return {"status": "completed"}
    else:
        return {"error": "Host not allowed"}