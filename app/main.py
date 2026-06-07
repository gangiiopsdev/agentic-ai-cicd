from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    args = ['ping', host]
    subprocess.run(args, check=True)

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)