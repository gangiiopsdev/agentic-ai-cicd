from fastapi import FastAPI
import subprocess
dfrom shlex import quote

app = FastAPI()

def escape_host(host):
    # Properly escape the host to prevent command injection
    return quote(host)

@app.get("/ping")
def ping(host: str):
    escaped_host = escape_host(host)
    subprocess.call(['ping', '-c', '1', escaped_host])
    return {"status": "completed"}