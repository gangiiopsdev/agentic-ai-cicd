from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    if not host:
        return "Host parameter missing"
    cmd_parts = ['ping', *shlex.split(host)]
    try:
        subprocess.run(cmd_parts, check=True)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)