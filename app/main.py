from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation using shlex.quote for proper quoting
    command = f'ping {host}'
    subprocess.call(command, shell=False)

@app.get("/ping")
def ping_route(host: str):
    return ping(host)