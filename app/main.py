from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Fixed implementation using shlex.quote to prevent shell injection
    subprocess.call(['ping', shlex.quote(host)])

@app.get("/ping")
def ping_route(host: str):
    return ping(host)

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}