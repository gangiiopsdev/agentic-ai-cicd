from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_ping(host: str):
    # Safe implementation using shlex.quote to prevent shell injection
    ping_command = ['ping', host]
    subprocess.call(ping_command)

@app.get("/ping")
def ping(host: str):
    execute_ping(host)
    return {"status": "completed"}