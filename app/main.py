from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if host in ["google.com", "bing.com"]:
        subprocess.call(['ping', host])
app = FastAPI()
@app.get("/ping")
def ping(host: str):    return {'status': 'not allowed'}