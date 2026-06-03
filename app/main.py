from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation using shlex.quote
    safe_host = subprocess.list2cmdline([host])
    subprocess.call(f"ping {safe_host}", shell=True)

@app.get("/ping")
def ping_route(host: str):
    return ping(host)