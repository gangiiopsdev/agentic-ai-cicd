from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation using shlex.quote to escape shell metacharacters
    from shlex import quote
    subprocess.call(['ping', quote(host)])

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}