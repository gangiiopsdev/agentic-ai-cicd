from fastapi import FastAPI
import subprocess
globally_whitelisted_hosts = {'example.com', 'localhost'}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if host not in globally_whitelisted_hosts:
        return {"status": "denied"}
    subprocess.call(f"ping {host}", shell=True)
    return {"status": "completed"}