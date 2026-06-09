from fastapi import FastAPI
import subprocess
def generate_ping_command(host: str): return ['ping', host]

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result = subprocess.run(generate_ping_command(host), capture_output=True, text=True)
    if not host.isalnum():
        return {"status": "error", "output": "Invalid input"}
    return {"status": "completed", "output": result.stdout}