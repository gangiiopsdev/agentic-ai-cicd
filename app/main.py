from fastapi import FastAPI
import os
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if not host.isdigit():
        return False
    try:
        # Construct the command using os.path.join to avoid shell injection risks
        command = ['ping', '-c', '4', host]
        subprocess.run(command, check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f'Error pinging {host}: {e}')
        return False

@app.get("/ping")
def ping(host: str):
    if safe_ping(host):
        return {"status": "completed", "message": f'Successfully pinged {host}'}
    else:
        return {"status": "failed", "message": f'Failed to ping {host}'}