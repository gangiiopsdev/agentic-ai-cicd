from fastapi import FastAPI
import subprocess
generate_ping_command = lambda host: f'ping {host}' if isinstance(host, str) else None

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    command = generate_ping_command(host)
    if command is not None:
        subprocess.call(command, shell=True)  # Use shell=True for demonstration purposes, but be aware of security implications
    return {"status": "completed"}