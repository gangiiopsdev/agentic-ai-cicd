from fastapi import FastAPI
import subprocess
global host_list
host_list = ['127.0.0.1', '::1']

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host in host_list:
        subprocess.call(f'ping {host}', shell=False)
        return {"status": "completed"}
    else:
        return {"error": "Invalid host"}