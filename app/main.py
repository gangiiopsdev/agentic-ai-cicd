from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Fixed implementation
    try:
        subprocess.call(shlex.split(f'ping -c 1 {shlex.quote(host)}'))
    except Exception as e:
        return {"error": str(e)}

    return {"status": "completed"}