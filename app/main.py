from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    try:
        args = shlex.split(f'ping {host}')
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f'Ping failed for {host}: {e}')
        return False

@app.get("/ping")
def ping(host: str):
    if safe_ping(host):
        return {"status": "completed", "ping_successful": True}
    else:
        return {"status": "completed", "ping_successful": False}