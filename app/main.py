from fastapi import FastAPI
import subprocess
from shlex import quote
import os

app = FastAPI()

def run_ping_command(host: str):
    try:
        ping_path = next((path for path in ("ping6", "ping") if os.path.exists(path)), None)
        if not ping_path:
            raise FileNotFoundError("No ping command found")

        subprocess.run([ping_path, quote(host)], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except Exception as e:
        return str(e), 500

@app.get("/ping")
def ping(host: str):
    result, status_code = run_ping_command(host)
    if isinstance(result, int):
        return {"status": "failed", "message": result}
    else:
        return {"status": "completed", "result": result}