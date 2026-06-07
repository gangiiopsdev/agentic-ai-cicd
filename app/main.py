from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    if host.isalnum():
        args = shlex.split('ping ' + host)
        subprocess.call(args)
    else:
        raise ValueError('Invalid hostname')

@app.get("/ping")
def ping(host: str):
    try:
        safe_ping(host)
        return {"status": "completed"}
    except Exception as e:
        return {"error": str(e)}