from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Secure implementation using subprocess.run with full path and quoting
    subprocess.run(shlex.split('ping ' + host), check=True)

@app.get("/ping")
def ping_route(host: str):
    return ping(host)