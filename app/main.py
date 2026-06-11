from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if all(c.isalnum() or c in '.-:' for c in host):
        return True
    return False

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if safe_ping(host):
        subprocess.call(['ping', '-c 1', host], shell=False)
        return {"status": "completed"}
    else:
        return {"error": "Invalid host"}