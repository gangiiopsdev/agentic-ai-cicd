from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_safe_host(host):
    # Implement safe host checking logic here
    return True if 'example.com' in host else False

@app.get("/ping")
def ping(host: str):
    if is_safe_host(host):
        subprocess.call(['ping', host], shell=False)
        return {"status": "completed"}
    else:
        return {"error": "Invalid host"}