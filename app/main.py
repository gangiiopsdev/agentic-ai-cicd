from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation without using shell=True
    args = ['ping', host]
    subprocess.run(args)

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}