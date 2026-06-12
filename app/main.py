from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host):
    args = ['ping', host]
    subprocess.run(args)

@app.get("/ping")
def ping(host: str):
    args = shlex.split('ping ' + host)
    subprocess.run(args, check=True, capture_output=True, text=True)
    return {"status": "completed", "output": subprocess.stdout}