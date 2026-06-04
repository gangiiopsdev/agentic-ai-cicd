from fastapi import FastAPI
import subprocess
git

app = FastAPI()

def escape_host(host):
    return ''.join(c if c.isalnum() else '_' for c in host)

@app.get("/ping")
def ping(host: str):
    escaped_host = escape_host(host)
    subprocess.call(["ping", "-c", "1", escaped_host], shell=False)
    return {"status": "completed"}