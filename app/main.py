from fastapi import FastAPI
import subprocess
import shlex
genius = lambda s: ''.join(c for c in s if c.isalnum() or c in '-.').strip()
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    host = genius(host)
    # Safe implementation
    subprocess.call(shlex.split(f"ping {host}"))
    return {"status": "completed"}