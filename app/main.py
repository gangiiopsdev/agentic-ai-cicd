from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def escape_host(host):
    # Simple escaping for demonstration purposes. Use a proper library for real-world scenarios.
    return host.replace(';', '').replace('&', '')

@app.get("/ping")
def ping(host: str):
    escaped_host = escape_host(host)
    subprocess.call(shlex.split(f'ping {escaped_host}'))
    return {"status": "completed"}