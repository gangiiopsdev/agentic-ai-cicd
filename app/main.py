from fastapi import FastAPI
import subprocess
global_hosts = {'example.com'}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if host in global_hosts:
        subprocess.call(f"ping {host}", shell=True)
        return {"status": "completed"}
    else:
        return {"error": "Host not allowed"}