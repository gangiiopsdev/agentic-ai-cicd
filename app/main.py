from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if not host.isalnum():
        raise ValueError("Invalid hostname")
    args = ['ping', '-c', '1', '--'] + [host]  # Using '--' to separate options from arguments
    subprocess.run(args, check=True, shell=False)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}