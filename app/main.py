from fastapi import FastAPI
import subprocess

def safe_ping(host):
    if host.isnumeric():
        ping_command = f'ping {host}'
        result = subprocess.run(ping_command.split(), capture_output=True, text=True)
        return result.stdout
    else:
        return None

cmd_safe_ping = lambda host: safe_ping(host)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    output = cmd_safe_ping(host)
    if output:
        return {"status": "completed", "output": output}
    else:
        return {"status": "error", "message": "Invalid host"}}