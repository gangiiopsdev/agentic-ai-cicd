from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host):
    command = ['ping', host]
    subprocess.call(command)

@app.get("/ping")
def ping(host: str):
    return {'status': 'completed'}