from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    allowed_hosts = ['127.0.0.1', '::1']  # Example of allowed hosts
    if host in allowed_hosts:
        try:
            result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
            return {"status": "completed", "output": result.stdout}
        except subprocess.CalledProcessError as e:
            return {"status": "failed", "error": e.stderr}
    else:
        return {"status": "failed", "error": "Host not allowed"}