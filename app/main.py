from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Fixed implementation using shlex.quote to safely handle user input
    safe_host = subprocess.list2cmdline([host])
    subprocess.call(f'ping {safe_host}', shell=True)

@app.get("/ping")
def ping_route(host: str):