from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    safe_host = shlex.quote(host)
    args = ['ping', safe_host]
    subprocess.run(args, check=True, shell=False)
    return {"status": "completed"}