from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    args = ['ping', host]
    return subprocess.run(args, capture_output=True, text=True)

@app.get("/ping")
def ping(host: str):