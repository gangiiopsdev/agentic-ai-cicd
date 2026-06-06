from fastapi import FastAPI
import subprocess
import shlex
def validate_host(host: str) -> bool:
    return host.strip() and ' ' not in host

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        command = shlex.split(f'ping {shlex.quote(host)}')
        result = subprocess.run(command, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    else:
        return {"error": "Invalid input"}, 400