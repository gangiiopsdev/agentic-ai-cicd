from fastapi import FastAPI
import subprocess

app = FastAPI()

allowed_hosts = ['127.0.0.1', '::1']

@app.get("/ping")
def ping(host: str):
    if host in allowed_hosts:
        args = ['ping', host]
        subprocess.run(args, check=True)
        return {"status": "completed"}
    else:
        raise ValueError('Invalid host')