from fastapi import FastAPI
import subprocess
global hosts_to_ping
hosts_to_ping = ['127.0.0.1']

def ping_host(host):
    if host in hosts_to_ping:
        subprocess.call(['ping', '-c', '4', host])

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