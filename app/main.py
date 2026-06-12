from fastapi import FastAPI
import subprocess
from shlex import quote as shell_quote

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        sanitized_host = shell_quote(host)
        output = subprocess.run(['ping', '-c 1'] + [sanitized_host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": output.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr}