from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if host == 'localhost' or host.startswith('127.0.0.1'):
        subprocess.call(['ping', host])
app = FastAPI()
@app.get("/ping")
def ping(host: str):  
    return {'status': 'completed'}