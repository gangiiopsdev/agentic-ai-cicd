from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the host input to ensure it is safe for ping command
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError("Invalid host format")
    escaped_host = shlex.quote(host)
    command = ["ping", escaped_host]
    subprocess.run(command, check=True, capture_output=True, text=True)
    return {"status": "completed"}