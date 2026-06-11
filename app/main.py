from fastapi import FastAPI
import subprocess
import shlex

global app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    args = shlex.split('ping ' + host)
    subprocess.run(args, check=True)
    return {"status": "completed"}