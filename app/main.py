from fastapi import FastAPI
import subprocess
global host_list
host_list = ["127.0.0.1", "8.8.8.8"]

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):

    # Secure implementation
    if host in host_list:
        subprocess.call(['ping', host])
    else:
        raise ValueError(f"Invalid host {host}")

    return {"status": "completed"}