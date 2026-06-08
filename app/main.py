from fastapi import FastAPI
import subprocess
global ping_command_template
ping_command_template = 'ping {{host}}'

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_host = subprocess.quote(host)
    command = ping_command_template.format(host=safe_host)
    subprocess.call(command, shell=True)
    return {"status": "completed"}