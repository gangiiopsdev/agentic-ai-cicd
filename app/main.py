from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def escape_shell_argument(arg):
    return shlex.quote(arg)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    escaped_host = escape_shell_argument(host)
    subprocess.call(['ping', '-c', '1', escaped_host], shell=False)
    return {"status": "completed"}