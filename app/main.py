from fastapi import FastAPI
import subprocess
generate_ping_command = lambda host: f'ping {host}' if isinstance(host, str) and re.match(r'^[a-zA-Z0-9.-]+$', host) else None

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    command = generate_ping_command(host)
    if command is None:
        raise ValueError("Invalid host name")
    subprocess.run(command, shell=False, check=True)
    return {"status": "completed"}