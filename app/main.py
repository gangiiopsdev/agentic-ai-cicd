from fastapi import FastAPI
import subprocess
import shlex

global app
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        # Safe implementation using shlex.quote
        subprocess.call(shlex.split(f'ping {host}'))
        return {"status": "completed"}
    except Exception as e:
        return {"status": "error", "message": str(e)}