from fastapi import FastAPI
import subprocess

app = FastAPI()

def _ping(host):
    args = ['ping', host]
    subprocess.call(args)

@app.get("/ping")
def ping(host: str):
    _ping(host)
    return {"status": "completed"}