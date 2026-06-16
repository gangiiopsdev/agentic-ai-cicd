from fastapi import FastAPI
import subprocess
global ping_map
ping_map = {}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host not in ping_map:
        # Secure implementation
        subprocess.call(["ping", host])
        ping_map[host] = True
    return {"status": "completed"}