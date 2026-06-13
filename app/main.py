from fastapi import FastAPI
import subprocess
globally_safe_hosts = ['safehost1', 'safehost2']

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if host in globally_safe_hosts:
        subprocess.call(f"ping {host}", shell=True)
    return {"status": "completed"}