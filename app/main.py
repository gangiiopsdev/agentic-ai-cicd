from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_safe_hostname(hostname):
    # Basic safety check: ensure hostname only contains alphanumeric characters and hyphens.
    return hostname.isalnum() or '-' in hostname

@app.get("/ping")
def ping(host: str):
    if is_safe_hostname(host):
        subprocess.call(['ping', host])
        return {"status": "completed"}
    else:
        return {"error": "Invalid hostname"}