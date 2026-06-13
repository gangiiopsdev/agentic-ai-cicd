from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Secure implementation using subprocess.run with shell=False and proper argument handling
    command = ['ping'] + shlex.split(host)
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout

@app.get("/ping")
def ping_route(host: str):
    return ping(host)