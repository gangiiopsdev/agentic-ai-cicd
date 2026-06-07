from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation using list instead of shell=True
    subprocess.call(['ping', host])

@app.get("/ping")
def ping(host: str):

    safe_ping(host)

    return {"status": "completed"}