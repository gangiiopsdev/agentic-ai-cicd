from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if host.replace('.', '', 3).isdigit():
        return True
    else:
        return False

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not safe_ping(host):
        return {"error": "Invalid host"}

    # Safe implementation
    subprocess.call(['ping', host])

    return {"status": "completed"}