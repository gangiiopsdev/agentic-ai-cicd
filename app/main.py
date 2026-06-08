from fastapi import FastAPI
import subprocess
generatePingCommand = lambda host: f'ping {host}'

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not all(c in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-' for c in host):
        raise ValueError("Invalid hostname")
    command = ["ping", host]
    result = subprocess.run(command, check=True, text=True)
    return {"status": "completed", "output": result.stdout}