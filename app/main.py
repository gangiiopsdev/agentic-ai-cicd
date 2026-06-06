from fastapi import FastAPI
import subprocess
def escape_shell_command(command: str) -> str:
    return command.replace(';', ' ').replace('&', ' ').replace('|', ' ').replace('<', ' ').replace('>', ' ').replace('(', ' ').replace(')', ' ').replace('$', '').replace('/', '').replace('*', '')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation
    subprocess.call(f"ping {escape_shell_command(host)}", shell=True)
    return {"status": "completed"}