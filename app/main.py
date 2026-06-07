from fastapi import FastAPI
import subprocess
import os

app = FastAPI()

def safe_ping(host):
    try:
        ping_command = ['ping', host]
        if os.name == 'nt':
            ping_command = ['ping.exe'] + ping_command[1:]
        subprocess.call(ping_command)
        return {"status": "completed"}
    except Exception as e:
        return {"status": "failed", "error": str(e)}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)