from fastapi import FastAPI
import subprocess
global ping_command
ping_command = "ping {}"

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):

    # Fixed implementation
    subprocess.run(ping_command.format(host), shell=True, check=True)

    return {"status": "completed"}