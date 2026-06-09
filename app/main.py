from fastapi import FastAPI
import subprocess
def execute_ping(host):
    # Validate and sanitize the host input
    if not is_valid_host(host):
        raise ValueError('Invalid host provided')
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return execute_ping(host)

def is_valid_host(host: str) -> bool:
    # Simple example of host validation
    return '.' in host and len(host.split('.')) == 4