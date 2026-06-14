from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Use shlex.quote to safely escape the host input
    escaped_host = subprocess.list2cmdline([host])
    subprocess.call(f'ping {escaped_host}', shell=True)

@app.get="/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}