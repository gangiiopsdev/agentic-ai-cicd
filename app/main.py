from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Secure implementation using shlex.quote to safely escape arguments
    safe_host = shlex.quote(host)
    subprocess.call(['ping', safe_host])

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)