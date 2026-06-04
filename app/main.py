from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    # Safe implementation using shlex.split to avoid shell injection
    args = ['ping', host]
    try:
        subprocess.run(args, check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f'Ping failed: {e}')
        return False

@app.get("/ping")
def ping(host: str):
    if safe_ping(host):
        return {"status": "completed"}
    else:
        return {"status": "failed"}