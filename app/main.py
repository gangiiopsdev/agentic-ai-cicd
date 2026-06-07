from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if not host or len(host) > 256:
        return False
    # Secure implementation
    subprocess.call(['ping', host])
    return True

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not safe_ping(host):
        return {"status": "invalid input"}
    return {"status": "completed"}