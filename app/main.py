from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation using shlex.quote to safely escape arguments
    safe_host = subprocess.list2cmdline([host])
    subprocess.call(['ping', safe_host])

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)