from fastapi import FastAPI
import subprocess
global_ping_command = "ping {}

app = FastAPI()

@app.get('/')
def home():
    return {"message": 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Safe implementation
    subprocess.call(global_ping_command.format(host), shell=True)
    return {"status": 'completed'}