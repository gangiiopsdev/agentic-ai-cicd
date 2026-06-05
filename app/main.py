from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping_safe(host: str):
    args = ['ping', host]
    subprocess.call(args, shell=False)

@app.get("/ping")
def ping(host: str):
    return ping_safe(host)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}