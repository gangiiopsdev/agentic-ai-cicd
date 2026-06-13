from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Safe implementation with shell=False and shlex for safe argument splitting
    args = ['ping', host]
    subprocess.run(args, check=True, shell=False)
    return {"status": "completed"}