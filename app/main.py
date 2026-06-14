from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Secure implementation using shlex to safely split the command string
    args = ['ping'] + shlex.split(host)
    if len(args) > 1:
        raise ValueError('Invalid input detected')
    subprocess.run(args, check=True)

@app.get("/ping")
def ping_route(host: str):
    return ping(host)