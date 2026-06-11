from fastapi import FastAPI
import subprocess
generate_ping_command = lambda host: f'ping {host}' if isinstance(host, str) and len(host.split()) == 1 else None

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    command = generate_ping_command(host)
    if command:
        subprocess.run(command, shell=False)
    return {"status": "completed"}