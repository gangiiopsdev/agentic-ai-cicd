from fastapi import FastAPI
import subprocess
generate_ping_command = lambda host: ["ping", host]

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent command injection
    if not host.isalnum() or len(host) > 255:
        return {"status": "error", "message": "Invalid host name"}
    subprocess.call(generate_ping_command(host), shell=False)
    return {"status": "completed"}