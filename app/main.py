from fastapi import FastAPI
import subprocess
import shlex
global app = FastAPI()
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
def ping(host: str):
    # Validate the host input to avoid command injection
    if not validate_host(host):
        return {"error": "Invalid host"}
    args = shlex.split(f'ping {host}')
    try:
        subprocess.run(args, check=True)
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}
def validate_host(host: str) -> bool:
    # Simple validation to allow only alphanumeric characters and a few special characters
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'
    return all(char in allowed_chars for char in host)
app.get("/home") = home
app.get("/ping") = ping