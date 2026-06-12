from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if not host or len(host) > 255:
        raise ValueError("Invalid host")
    args = ['ping', '--'] + [host]
    subprocess.run(args, check=True)
app = FastAPI()
@app.get("/ping")
def ping(host: str):