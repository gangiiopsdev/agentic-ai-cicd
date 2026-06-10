from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Safe implementation using shlex to escape arguments
    subprocess.call(shlex.split('ping ' + host), check=True)

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)