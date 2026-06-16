from fastapi import FastAPI
import subprocess
global host_set
host_set = {'example.com'}

def check_host(host):
    if host in host_set:
        return True
    else:
        raise Exception("Invalid host")

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):

    if check_host(host):
        # Safer implementation
        subprocess.call(["ping", host])
        return {"status": "completed"}