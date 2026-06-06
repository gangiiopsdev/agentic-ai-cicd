from fastapi import FastAPI
import shlex
import subprocess
global app = FastAPI()
def safe_ping(host):
    # Safe implementation using shlex.split to avoid shell injection
    args = ['ping', host]
    try:
        result = subprocess.run(shlex.split(' '.join(args)), check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.returncode == 0
    except subprocess.CalledProcessError as e:
        print(f'Ping failed: {e.stderr.decode()})
        return False
@app.get("/ping")
def ping(host: str):
    if safe_ping(host):
        return {"status": "completed"}
    else:
        return {"status": "failed"}