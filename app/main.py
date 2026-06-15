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
    if command is None:
        return {"error": "Invalid host input"}, 400
    try:
        subprocess.call(command, shell=False)
        return {"status": "completed"}
    except Exception as e:
        return {"error": str(e)}, 500