from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    args = ['ping', host]
    return subprocess.run(args)

@app.get("/ping")
def ping(host: str):

    # Safe implementation
    result = safe_ping(host)
    if result.returncode == 0:
        return {"status": "completed", "result": "Ping successful"}
    else:
        return {"status": "failed", "result": "Ping failed"}