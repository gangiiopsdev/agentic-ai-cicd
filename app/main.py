from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        # Splitting the host argument prevents command injection
        subprocess.call(['ping', host], shell=False)
        return True
    except Exception as e:
        print(e)
        return False

@app.get("/ping")
def ping(host: str):
    if safe_ping(host):
        return {"status": "completed"}
    else:
        return {"status": "failed", "error": "Invalid host"}