from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    # Use shell=False and safely pass arguments
    args = ['ping'] + shlex.split(host)
    subprocess.call(args, shell=False)

@app.get("/ping")
def ping(host: str):
    # Call the safe function instead of directly invoking subprocess
    safe_ping(host)
    return {"status": "completed"}