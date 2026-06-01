from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host):
    cmd = ['ping', host]
    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        print(f'Ping failed: {e}')

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}