from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host):
    args = ['ping', host]
    return subprocess.run(shlex.split(' '.join(args)), capture_output=True, text=True)

@app.get("/ping")
def ping(host: str):
    if not host.isalnum():
        raise ValueError("Invalid host provided")
    result = safe_ping(host)
    return {"status": "completed", "stdout": result.stdout}