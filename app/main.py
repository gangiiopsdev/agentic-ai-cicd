from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize the input to prevent command injection
    sanitized_host = shlex.quote(host)
    command = ['ping', sanitized_host]
    subprocess.run(command, check=True)
    return {"status": "completed"}