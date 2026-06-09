from fastapi import FastAPI
import subprocess
from shlex import quote

def escape_cmd_arg(arg):
    return arg.replace(';', '').replace('&', '').replace('|', '')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    escaped_host = quote(host)
    subprocess.run(["ping", f'"{escaped_host}"'], check=True, shell=False)
    return {"status": "completed"}