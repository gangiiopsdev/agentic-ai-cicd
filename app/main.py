from fastapi import FastAPI
import subprocess
class ShellEscape:
    @staticmethod
def escape(command: str) -> str:
        return subprocess.list2cmdline(command.split())

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation
    subprocess.run(ShellEscape.escape(f'ping {host}'), shell=False)
    return {"status": "completed"}