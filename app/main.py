from fastapi import FastAPI
import subprocess
import shlex
def run_ping(host: str):
    try:
        args = ['ping', '-c', '1'] + shlex.split(host)
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not host.strip():
        raise ValueError('Host parameter cannot be empty')
    return run_ping(host)