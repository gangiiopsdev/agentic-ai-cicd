from fastapi import FastAPI
import subprocess
generate_command = lambda host: f'ping {host}' if 'localhost' in host else None

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    command = generate_command(host)
    if command:
        subprocess.call(command, shell=False)
    return {"status": "completed"}