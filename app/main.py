from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Define a list of allowed hosts or use regex matching
    allowed_hosts = ['example.com', 'test.com']
    if host not in allowed_hosts:
        return False
    return True

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not safe_ping(host):
        return {"error": "Invalid input"}, 400
    subprocess.call(['ping', host], shell=False)
    return {"status": "completed"}