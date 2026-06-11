from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    allowed_hosts = ['8.8.8.8', '127.0.0.1']
    if host in allowed_hosts:
        try:
            output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=5)
            return {"status": "completed", "output": output.decode()}
        except subprocess.CalledProcessError as e:
            return {"status": "failed", "error": e.output.decode()}
    else:
        return {"status": "failed", "error": "Host not allowed"}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)