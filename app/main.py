from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation using subprocess.call without shell=True
    try:
        subprocess.run(['ping', host], check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f'Ping failed with error: {e}')
        return False

@app.get("/ping")
def ping(host: str):
    if safe_ping(host):
        return {"status": "completed", "result": True}
    else:
        return {"status": "failed", "result": False}