from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host):
    cmd = ['ping', host]
    try:
        subprocess.run(cmd, check=True, shell=False)
    except subprocess.CalledProcessError as e:
        print(f'Ping failed: {e}')
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}