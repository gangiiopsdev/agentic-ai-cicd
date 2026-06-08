from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def is_valid_host(host):
    # Basic validation for demonstration purposes
    return host.strip() and not any(char in host for char in [';', '&', '|'])

@app.get("/ping")
def ping(host: str):
    if is_valid_host(host):
        args = shlex.split(f"ping {host}")
        subprocess.call(args)
        return {"status": "completed"}
    else:
        return {"status": "invalid host", "error": "Host contains invalid characters"}