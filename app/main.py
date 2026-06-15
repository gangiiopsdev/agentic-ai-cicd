from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_host(host):
    # Basic escaping to avoid simple injection
    return host.replace(';', '').replace('&', '')

@app.get("/ping")
def ping(host: str):
    escaped_host = escape_host(host)
    subprocess.call(f"ping \\{escaped_host\\}", shell=False)
    return {"status": "completed"}