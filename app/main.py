from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host):
    args = ['ping', host]
    subprocess.run(args, check=True)

@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        safe_ping(shlex.quote(host))
        return {"status": "completed"}
    else:
        return {"status": "invalid host", "error": "Invalid hostname provided."}, 400

def validate_host(host):
    import re
    pattern = re.compile(r'^[a-zA-Z0-9.-]+$')
    return bool(pattern.match(host))