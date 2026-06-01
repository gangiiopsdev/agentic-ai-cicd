from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    safe_host = subprocess.list2cmdline([host])
    subprocess.call(['ping', safe_host], shell=False)
    return {"status": "completed"}