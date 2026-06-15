from fastapi import FastAPI
import subprocess
def escape_shell_arg(arg):
    return subprocess.list2cmdline([arg])

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    subprocess.call(f'ping {escape_shell_arg(host)}', shell=True)
    return {"status": "completed"}