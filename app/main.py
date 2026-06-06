from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_shell_argument(arg):
    return subprocess.list2cmdline([arg])

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    subprocess.call(escape_shell_argument(f'ping {host}'))
    return {"status": "completed"}