from fastapi import FastAPI
import subprocess
generate_ping_command = lambda host: ['ping', host]

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate input to ensure it's safe for the ping command
    if not host.isalnum() or len(host) > 255:
        raise ValueError('Invalid host name')
    subprocess.call(generate_ping_command(host))
    return {"status": "completed"}