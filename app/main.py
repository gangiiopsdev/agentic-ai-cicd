from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_shell_command(command):
    return ' '.join(subprocess.list2cmdline(arg) for arg in command.split())

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):

    # Fixed implementation
    subprocess.call(escape_shell_command(f"ping {host}"), shell=True)

    return {"status": "completed"}