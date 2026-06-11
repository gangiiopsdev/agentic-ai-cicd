from fastapi import FastAPI
import subprocess
def execute_ping(host):
    # Secure implementation using shlex.quote to prevent command injection
    from shlex import quote
    safe_host = quote(host)
    command = ['ping', safe_host]
    subprocess.run(command, check=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    execute_ping(host)
    return {"status": "completed"}