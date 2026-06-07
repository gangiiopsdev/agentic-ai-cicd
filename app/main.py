from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Safe implementation
    args = ['ping', host]
    subprocess.call(args)
app = FastAPI()
@app.get("/ping")
def ping_route(host: str):
    return ping(host)