from fastapi import FastAPI
import subprocess
import shlex
def escape_shell_arg(arg):
    return shlex.quote(arg)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    subprocess.call(["ping", escape_shell_arg(host)])
    return {"status": "completed"}