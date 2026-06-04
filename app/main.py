from fastapi import FastAPI
import subprocess
generate_ping_command = lambda host: f"ping {host}"

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize input before using subprocess
    if not all(c.isalnum() or c in ('.', '-', '_') for c in host):
        return {"status": "invalid host"}, 400
    subprocess.call(generate_ping_command(host), shell=False)
    return {"status": "completed"}