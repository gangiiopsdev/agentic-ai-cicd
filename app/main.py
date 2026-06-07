from fastapi import FastAPI
import subprocess
def execute_ping(host):
    args = ['ping', host]
    subprocess.run(args, check=True)

app = FastAPI()

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    if not host.isnumeric():  # Simple validation to ensure the input is numeric (a common ping target)
        raise ValueError("Invalid host")
    execute_ping(host)
    return {"status": "completed"}