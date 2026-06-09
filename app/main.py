from fastapi import FastAPI
import subprocess
def escape_host(host: str):
    return host.replace(';', '').replace('&', '')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    escaped_host = escape_host(host)
    command = ['ping', escaped_host]
    subprocess.run(command, check=True, shell=False)
    return {"status": "completed"}