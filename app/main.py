from fastapi import FastAPI
import subprocess
def run_ping(host):
    args = ['ping', host]
    subprocess.call(args)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    run_ping(host)
    return {"status": "completed"}