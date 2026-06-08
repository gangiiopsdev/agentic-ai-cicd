from fastapi import FastAPI
import subprocess
import shlex

global app
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        # Using shlex.split to safely split the command into arguments
        args = shlex.split(f"ping {host}")
        subprocess.call(args)
        return {"status": "completed"}
    except Exception as e:
        return {"error": str(e), "status": "failed"}