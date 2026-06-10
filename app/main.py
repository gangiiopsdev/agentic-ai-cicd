from fastapi import FastAPI
import subprocess

app = FastAPI()

allowed_hosts = ['127.0.0.1', '::1']

@app.get("/ping")
def ping(host: str):
    if host not in allowed_hosts:
        return {"status": "failed", "error": "Invalid host"}
    try:
        # Using subprocess.run to avoid shell=True and with absolute path for security
        result = subprocess.run(['/sbin/ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed", "output": result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr.decode()}