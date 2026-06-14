from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(user_input):
    return shlex.quote(user_input)

def escape_shell_arg(arg):
    return subprocess.list2cmdline([arg])

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):