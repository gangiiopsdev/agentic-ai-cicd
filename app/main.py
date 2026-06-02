from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host):
    # Safe implementation using shlex for argument quoting
    args = shlex.split('ping ' + host)
    subprocess.run(args, check=True)

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}