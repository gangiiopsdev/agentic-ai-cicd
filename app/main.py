from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def is_valid_host(host: str) -> bool:
    # Implement your validation logic here
    return host.isdigit() and len(host) == 1

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the host input to prevent command injection
    if not is_valid_host(host):
        return {"status": "error", "message": "Invalid host"}

    # Use shlex.quote to safely quote the host parameter
    result = subprocess.run(["ping", shlex.quote(host)], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}