from fastapi import FastAPI
import subprocess
from shlex import quote as cmd_quote

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.run with shell=False and check=True
    try:
        subprocess.run(["ping", cmd_quote(host)], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}