from fastapi import FastAPI
import subprocess
import shlex
def escape_shell_arg(arg):
    return shlex.quote(str(arg))
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    # Validate and sanitize input
    if not host.isalnum() or len(host) > 100:
        raise ValueError("Invalid hostname")
    subprocess.run(shlex.split(f'ping {escape_shell_arg(host)}'), check=True)
    return {"status": "completed"}