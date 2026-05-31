from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def escape_shell_arg(arg):
    return arg.replace(';', ' ').replace('&', ' ').replace('|', ' ') if isinstance(arg, str) else arg

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    args = ['ping', escape_shell_arg(host)]
    subprocess.call(shlex.split(' '.join(args)))
    return {"status": "completed"}