from fastapi import FastAPI
import subprocess
from shlex import quote

def execute_ping(host: str):
    # Sanitize the host input to prevent command injection
    safe_host = quote(host)
    args = ['ping', safe_host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return execute_ping(host)