from fastapi import FastAPI
import subprocess

app = FastAPI()

def generate_ping_command(host: str) -> list:
    return ['ping', host]

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the input to ensure it does not contain malicious content
    if any(char in host for char in '><&;`\':"	
\x00'):  # Simple validation, improve as needed
        return {"status": "invalid_host", "message": "Invalid host provided"}
    subprocess.call(generate_ping_command(host))
    return {"status": "completed"}