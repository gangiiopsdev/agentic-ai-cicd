from fastapi import FastAPI
import subprocess
generate_ping_command = lambda host: f'ping {host}'

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        raise ValueError("Invalid host")
    subprocess.call(generate_ping_command(host), shell=False)
    return {"status": "completed"}

def validate_host(host: str) -> bool:
    # Add logic to validate the host input
    allowed_hosts = ["example.com", "test.example.com"]
    return host in allowed_hosts