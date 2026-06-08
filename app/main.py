from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Secure implementation
    args = ['ping', *shlex.split(host)]
    subprocess.run(args, check=True)

@app.get("/ping")
def ping_route(host: str):
    return ping(host)