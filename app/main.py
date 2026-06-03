from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    if not host:
        return "Host parameter missing"
    cmd_parts = ['ping', *shlex.split(host)]
    try:
        result = subprocess.run(cmd_parts, capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"error": str(e), "stderr": e.stderr}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)