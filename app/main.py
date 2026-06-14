from fastapi import FastAPI
import subprocess
globally_safe_hosts = ['safehost1', 'safehost2']

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if host in globally_safe_hosts:
        subprocess.call(['ping', host])  # Use list instead of shell=True
    return {"status": "completed"}