from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Safe implementation with shlex for better safety
    args = ['ping', host]
    subprocess.call(shlex.split(' '.join(args)))

@app.get("/ping")
def ping_handler(host: str):
    return ping(host)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}