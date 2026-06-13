from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    args = ['ping', *shlex.split(host)]
    subprocess.run(args, check=True)

@app.get("/ping")
def ping_endpoint(host: str):
    result = ping(host)
    return {"status": "completed"}