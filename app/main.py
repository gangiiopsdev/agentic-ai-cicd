from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Secure implementation using shlex.quote to escape arguments
    command = ['ping', shlex.quote(host)]
    subprocess.run(command, check=True)

@app.get("/ping")
def ping_route(host: str):    return ping(host)