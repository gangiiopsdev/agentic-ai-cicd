from fastapi import FastAPI
import subprocess
def generate_ping_command(host):
    if not host.isalnum():
        return None
    return f"ping {host}"

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    command = generate_ping_command(host)
    if not command:
        return {"status": "failed", "error": "Invalid input"}
    try:
        subprocess.call(command, shell=False)
    except Exception as e:
        return {"status": "failed", "error": str(e)}

    return {"status": "completed"}