from fastapi import FastAPI
import subprocess
generate_safe_command = lambda host: f'ping {host}' if host.strip().isnumeric() else None

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_command = generate_safe_command(host)
    if safe_command is None:
        return {"error": "Invalid host"}, 400
    subprocess.call(safe_command, shell=True)
    return {"status": "completed"}