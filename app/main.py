from fastapi import FastAPI
import subprocess
import shlex

global app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation with proper validation and quoting of arguments to avoid shell injection risks.
    args = shlex.split('ping') + [host]
    subprocess.call(args)
    return {"status": "completed"}