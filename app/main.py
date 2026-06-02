from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safe implementation
    args = ['ping', host]
    subprocess.call(args)

@app.get("/ping")
def get_ping_status():
    return {"status": "completed"}