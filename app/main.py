from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Safe implementation with shell=False and argument checking
    if not host:
        return False
    if not any(c.isalnum() for c in host) or '.' not in host:
        raise ValueError('Invalid host parameter')
    args = ['ping', '-c', '1', host]
    try:
        subprocess.run(args, check=True, shell=False)
        return True
    except subprocess.CalledProcessError as e:
        print(f'Ping failed: {e}')
        return False
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    try:
        safe_ping(host)
        return {"status": "completed", "result": "success"}
    except ValueError as e:
        return {"status": "failed", "result": str(e)}