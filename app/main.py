from fastapi import FastAPI
import subprocess
from urllib.parse import urlparse
import shlex

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate the input to prevent command injection
    parsed_url = urlparse(host)
    if not parsed_url.hostname or '||' in host or ';' in host:
        raise ValueError("Invalid host URL")
    subprocess.run(shlex.split(f"ping {parsed_url.hostname}"), check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {"status": "completed"}