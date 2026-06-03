from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    args = ['ping', host]
    subprocess.run(args, check=True)

@app.get("/ping")
def ping_handler(host: str):
    return ping(host)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}