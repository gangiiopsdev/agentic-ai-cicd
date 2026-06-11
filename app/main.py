from fastapi import FastAPI
import subprocess
import shlex
def validate_host(host: str) -> bool:
    return host.isalnum() and len(host) <= 255

def sanitize_input(user_input: str) -> str:
    return user_input.replace("&", "").replace("|", "")

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {"error": "Invalid host name"}
    sanitized_host = sanitize_input(host)
    try:
        subprocess.run(shlex.split(f'ping {sanitized_host}'), check=True)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}