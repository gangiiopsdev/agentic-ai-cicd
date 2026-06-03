from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    if host in ['localhost', '127.0.0.1']:  # Allow only known safe hosts
        command = ['ping'] + shlex.split(host)
        subprocess.call(command, shell=False)
    else:
        raise ValueError('Unsafe host')

@app.get("/ping")
def ping(host: str):
    try:
        safe_ping(host)
        return {"status": "completed"}
    except Exception as e:
        return {"error": str(e)}, 400