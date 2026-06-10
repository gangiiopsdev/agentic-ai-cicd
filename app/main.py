from fastapi import FastAPI
import subprocess
generate_ping_command = lambda host: f'ping {host}' if host.isnumeric() else None
def safe_ping(host):
    ping_command = generate_ping_command(host)
    if ping_command:
        result = subprocess.run(ping_command.split(), capture_output=True, text=True, check=True)
        return result.stdout
    else:
        raise ValueError("Invalid host")

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        output = safe_ping(host)
        return {"status": "completed", "output": output}
    except ValueError as e:
        return {"status": "error", "message": str(e)}```