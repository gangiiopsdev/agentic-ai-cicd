from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Fixed implementation with validation
    if not host or not host.strip():
        raise ValueError('Host cannot be empty')
    args = ['ping', '-c', '1']
    args.append(subprocess.list2cmdline([host]))
    subprocess.run(args, check=True)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_safe(host: str):
    ping(host)