from fastapi import FastAPI
import subprocess
generate_ping_command = lambda host: f'ping {host}' if isinstance(host, str) and all(c.isalnum() or c in ('.', '-', '_') for c in host) else None

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    command = generate_ping_command(host)
    if command:
        subprocess.call(command, shell=True)
    return {"status": "completed"}