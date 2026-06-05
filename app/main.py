from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host):
    # Safe implementation using subprocess.run with properly quoted args
    cmd = ['ping', host]
    cmd_str = ' '.join(shlex.quote(arg) for arg in cmd)
    subprocess.run(cmd_str, shell=True, capture_output=True, text=True)

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}