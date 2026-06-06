from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation using Popen
    args = ['ping', host]
    subprocess.Popen(args)

@app.get("/ping")
def ping_route(host: str):  
    return ping(host)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}