from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    if host.startswith('localhost') or host.startswith('127.0.0.1'):
        return subprocess.run(['ping', shlex.quote(host)], capture_output=True, text=True, check=True)
    else:
        raise ValueError("Unsafe ping request")

@app.get("/ping")
def ping(host: str):
    try:
        output = safe_ping(host)
        return {"status": "completed", "output": output.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}