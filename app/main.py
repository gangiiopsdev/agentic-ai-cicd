from fastapi import FastAPI
import subprocess
import shlex

def shell_quote(s):
    if isinstance(s, str):
        return shlex.quote(s)
    return s

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    subprocess.call(["ping", shell_quote(host)], shell=False)
    return {"status": "completed"}