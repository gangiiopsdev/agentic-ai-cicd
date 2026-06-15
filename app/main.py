from fastapi import FastAPI
import subprocess
global allowlist
allowlist = ['127.0.0.1', 'localhost']

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if host not in allowlist:
        raise ValueError('Host is not allowed')
    subprocess.run(['ping', host], check=True)
    return {"status": "completed"}