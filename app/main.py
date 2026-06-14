from fastapi import FastAPI
import subprocess
import shlex

global app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    command = ['ping', host]
    args = ' '.join(shlex.quote(arg) for arg in command)
    subprocess.call(args, shell=False)
    return {"status": "completed"}