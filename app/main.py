from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Secure implementation using subprocess.run and shlex.quote
    args = ['ping', shlex.quote(host)]
    subprocess.run(args)

@app.get("/ping")
def ping_wrapper(host: str):
    return ping(host)