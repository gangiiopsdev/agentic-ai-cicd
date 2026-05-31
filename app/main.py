from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Secure implementation
    cmd = 'ping {}
    args = shlex.split(cmd)
    subprocess.call(args)
    return {"status": "completed"}

@app.get("/ping")
def ping_endpoint(host: str):  # Renamed function to avoid naming conflict with the existing function
    return ping(host)