from fastapi import FastAPI
import subprocess
def escape_shell_arg(arg):
    return ' '.join([subprocess.list2cmdline(a) for a in arg.split()])

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    subprocess.call(escape_shell_arg(f"ping {host}"))
    return {"status": "completed"}