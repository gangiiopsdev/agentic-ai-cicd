from fastapi import FastAPI
import subprocess
def generate_ping_command(host):
    return f'ping {host}'

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    command = generate_ping_command(host)
    if command.startswith('ping '):
        subprocess.call(command.split(), shell=False)
    return {"status": "completed"}