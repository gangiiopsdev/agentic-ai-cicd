from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if host.isnumeric() and '.' in host:
        cmd = ['ping', host]
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.stdout
app = FastAPI()
@app.get("/ping")
def ping(host: str):    return safe_ping(host)