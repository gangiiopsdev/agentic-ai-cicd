from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_safe_host(host):
    allowed_hosts = ['127.0.0.1', '::1']  # Define a list of safe hosts
    return host in allowed_hosts

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        return {"status": "failed", "error": "Unsafe host provided"}
    try:
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed", "output": result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr.decode()}