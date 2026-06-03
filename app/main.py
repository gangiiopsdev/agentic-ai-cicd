from fastapi import FastAPI
import subprocess
def escape_cmd_arg(arg):
    return arg.replace(';', '').replace('&', '').replace('|', '')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    escaped_host = escape_cmd_arg(host)
    subprocess.call(["ping", escaped_host])
    return {"status": "completed"}