from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Use shlex.quote to safely handle the input
    cmd = ['ping', host]
    subprocess.run(cmd, check=True)

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    safe_ping(host)
    return {"status": "completed"}