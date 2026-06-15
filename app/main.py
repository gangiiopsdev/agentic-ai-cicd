from fastapi import FastAPI
import subprocess
def escape_shell_arg(arg):
    return ''.join(c if c.isalnum() else f'\{ord(c):03o}' for c in arg)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not host.strip():
        raise ValueError("Host parameter cannot be empty or contain only whitespace.")
    subprocess.run(['ping', escape_shell_arg(host)], check=True)
    return {"status": "completed"}