from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    generate_ping_command = ['ping', host]
    # Validate the host input to ensure it does not contain malicious content
    if not is_valid_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    subprocess.run(generate_ping_command, check=True)
    return {'status': 'completed'}

def is_valid_host(host: str) -> bool:
    # More comprehensive validation
    import re
    pattern = re.compile(r'^[a-zA-Z0-9.-_]+$')
    return bool(pattern.match(host))

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return ping(host)