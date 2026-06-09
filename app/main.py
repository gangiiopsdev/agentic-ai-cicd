from fastapi import FastAPI
import subprocess
import shlex

global app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    cmd = ['ping', host]
    subprocess.run(cmd, check=True, capture_output=True)
    return {"status": "completed"}