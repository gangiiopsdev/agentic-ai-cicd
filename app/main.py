from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def ping(host: str):
    # Secure implementation
    args = ['ping', quote(host)]
    subprocess.run(args, check=True, timeout=5)

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)