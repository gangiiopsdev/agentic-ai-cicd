from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate input to prevent command injection
    if not host.isalnum() or len(host) > 255:
        return {"error": "Invalid host name"}, 400

    # Secure implementation
    command = ['ping', shlex.quote(host)]
    subprocess.run(command, check=True)

    return {"status": "completed"}