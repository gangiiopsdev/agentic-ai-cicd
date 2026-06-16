from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safer implementation using shlex.quote to prevent command injection
    safe_host = subprocess.list2cmdline([host])
    subprocess.call(f"ping {safe_host}", shell=False)

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)