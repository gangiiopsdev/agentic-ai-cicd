from fastapi import FastAPI
import subprocess
def execute_ping(host):
    # Use shlex.quote to safely escape command arguments
    safe_host = subprocess.shlex_quote(host)
    subprocess.call(f"ping {safe_host}")

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    execute_ping(host)
    return {"status": "completed"}