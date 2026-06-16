from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping_host(host: str):
    # Secure implementation using subprocess.Popen
    args = ['ping', host]
    subprocess.run(args, check=True)

@app.get("/ping")
def ping(host: str):
    return ping_host(host)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}