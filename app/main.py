from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate host to ensure it does not contain malicious input
    allowed_hosts = ['example.com', 'localhost']
    if host in allowed_hosts:
        subprocess.call(['ping', host], shell=False)
        return {"status": "completed"}
    else:
        return {"error": "Invalid host"}