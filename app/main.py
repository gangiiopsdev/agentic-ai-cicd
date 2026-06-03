from fastapi import FastAPI
import subprocess
import shlex
global host_list
host_list = ['192.168.0.1', '8.8.8.8']

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host in host_list:
        try:
            args = shlex.split(f'ping {host}')
            subprocess.call(args)
            return {"status": "completed"}
        except Exception as e:
            return {"error": str(e)}
    else:
        return {"error": "Host not allowed"}