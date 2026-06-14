from fastapi import FastAPI
import subprocess
import shlex
global hosts_to_ping
hosts_to_ping = ['127.0.0.1']

def ping_host(host):
    if host in hosts_to_ping:
        args = ['ping', '-c', '4'] + shlex.split(host)
        subprocess.call(args)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        ping_host(host)
        return {"status": "completed"}
    except Exception as e:
        return {"error": str(e)}