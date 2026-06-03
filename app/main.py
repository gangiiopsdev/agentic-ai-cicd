from fastapi import FastAPI
import subprocess
import shlex

global app
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    cmd = ['ping', host]
    subprocess.run(cmd, check=True)
    return {"status": "completed"}