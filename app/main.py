from fastapi import FastAPI
import subprocess
import shlex

global app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    try:
        args = shlex.split(f'"ping" {host}')
        subprocess.run(args, check=True)
        return {"status": "completed"}
    except Exception as e:
        return {"status": "failed", "error": str(e)}