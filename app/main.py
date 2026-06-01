from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Safe implementation using subprocess.Popen instead of shell=True
    args = ['ping', host]
    result = subprocess.Popen(args)
    result.wait()
app = FastAPI()
@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)