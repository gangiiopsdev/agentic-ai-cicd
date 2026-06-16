from fastapi import FastAPI
import subprocess
import shlex
global_safe_host = 'localhost'  # or any trusted default host

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize the input to prevent command injection
    safe_host = shlex.quote(host)
    subprocess.run(['ping', global_safe_host], check=True, env={'HOST': safe_host})
    return {"status": "completed"}