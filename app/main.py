from fastapi import FastAPI
import subprocess

def generate_ping_command(host: str) -> list:
    return ["ping", host]

def ping(host: str):
    if not is_valid_host(host):
        raise ValueError("Invalid host")
    result = subprocess.run(generate_ping_command(host), capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return ping(host)

def is_valid_host(host: str) -> bool:
    # Add logic to validate the host input
    return True