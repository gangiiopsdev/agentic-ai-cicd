from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if host.isnumeric():
        subprocess.call(["ping", host])
    else:
        return "Invalid input"
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    return safe_ping(host)