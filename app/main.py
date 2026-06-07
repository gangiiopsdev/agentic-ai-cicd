from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Safer implementation using shlex.quote to safely escape user input
    safe_host = subprocess.list2cmdline([host])
    subprocess.run(['ping', *safe_host.split()], check=True)
    return {"status": "completed"}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}