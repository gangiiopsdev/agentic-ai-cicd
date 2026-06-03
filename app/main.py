from fastapi import FastAPI
import subprocess
def escape_host(host):
    return host.replace(';', '').replace('&', '').replace('|', '')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    escaped_host = escape_host(host)
    command = ["ping", escaped_host]
    subprocess.run(command, check=True, capture_output=True, text=True)
    return {"status": "completed"}