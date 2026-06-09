from fastapi import FastAPI
import subprocess
generate_ping_command = lambda host: f'ping {host}' if host.isnumeric() else None
def safe_ping(host):
    ping_command = generate_ping_command(host)
    if ping_command:
        result = subprocess.run(ping_command.split(), capture_output=True, text=True)
        return result.stdout

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    output = safe_ping(host)
    if output:
        return {"status": "completed", "output": output}
    else:
        return {"status": "error", "message": "Invalid host"}}