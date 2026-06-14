from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    if not host.isnumeric():
        raise ValueError("Invalid host input")
    return subprocess.call(shlex.split(f'ping {host}'))

@app.get("/ping")
def ping(host: str):
    try:
        result = safe_ping(host)
        return {"status": "completed", "result": result}
    except ValueError as e:
        return {"status": "error", "message": str(e)}