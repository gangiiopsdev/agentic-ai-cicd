from fastapi import FastAPI
import subprocess
generate_ping_command = ['ping', '{}']

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent command injection
    sanitized_host = host.strip()
    if not all(c.isalnum() or c in [',', '.', '-', '_'] for c in sanitized_host):
        return {"status": "error", "message": "Invalid host name"}
    subprocess.call(generate_ping_command.format(sanitized_host))
    return {"status": "completed"}