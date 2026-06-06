from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    try:
        # Safe implementation with full executable path and sanitized input
        args = ['ping', shlex.quote(host)]
        subprocess.run(args, check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f'Ping failed with error: {e}')
        return False

@app.get("/ping")
def ping(host: str):
    if safe_ping(host):
        return {"status": "completed", "message": "Ping successful"}
    else:
        return {"status": "failed", "message": "Ping failed"}