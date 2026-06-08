from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    allowed_hosts = ['127.0.0.1', 'localhost']
    return host in allowed_hosts

@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        subprocess.run(['ping', host], check=True)
        return {"status": "completed"}
    else:
        return {"error": "Invalid host"}