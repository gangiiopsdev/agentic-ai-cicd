from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation using Popen with argument splitting and shell=False
    args = ['ping', host]
    subprocess.Popen(args, shell=False)

@app.get("/ping")
def ping_route(host: str):  
    return {'host': host}

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}