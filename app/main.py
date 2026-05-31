from fastapi import FastAPI
import subprocess
import shlex

global host_blacklist = ['127.0.0.1', '::1']

def validate_host(host):
    if host in host_blacklist:
        raise ValueError("Invalid host")
    return host

app = FastAPI()

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    # Secure implementation
    validated_host = validate_host(shlex.quote(host))
    subprocess.call(["ping", validated_host])

    return {"status": "completed"}