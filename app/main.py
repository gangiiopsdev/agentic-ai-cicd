from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Secure implementation using subprocess.run instead of subprocess.call
    args = ['ping', host]
    subprocess.run(args, check=True, capture_output=True)

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)