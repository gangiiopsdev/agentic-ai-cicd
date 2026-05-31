from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    args = ['ping', host]
    subprocess.run(args)

@app.get("/ping")
def ping(host: str):

    # Safe implementation
    safe_ping(host)

    return {"status": "completed"}