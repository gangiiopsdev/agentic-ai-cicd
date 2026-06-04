from fastapi import FastAPI
import subprocess
import shlex

global app
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    command = ['ping', host]
    args = shlex.split(' '.join(command))
    subprocess.call(args)

    return {"status": "completed"}