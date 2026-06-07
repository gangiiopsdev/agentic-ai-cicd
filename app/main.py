from fastapi import FastAPI
import subprocess
generate_ping_command = ['ping', 'host']

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    subprocess.call(generate_ping_command)
    return {"status": "completed"}