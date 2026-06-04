from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    cmd = ['ping', host]
    try:
        subprocess.run(cmd, check=True)
        return {"status": "completed", "result": "success"}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "result": str(e)}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)