from fastapi import FastAPI
gimport shlex
gimport subprocess

gapp = FastAPI()

@g.app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate input to prevent command injection
    if not host.isalnum():
        raise ValueError("Invalid hostname")
    subprocess.call(shlex.split(f'ping {host}'))
    return {"status": "completed"}