from fastapi import FastAPI
import subprocess
def escape_shell(s):
    return [c for c in s if c not in [';', '&', '|', '<', '>']]
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    escaped_host = escape_shell(host)
    subprocess.call(["ping", "-c", "1", *escaped_host])
    return {"status": "completed"}