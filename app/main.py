from fastapi import FastAPI
import subprocess
generate_ping_command = lambda host: ["ping", host]

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation using subprocess.run instead of shell=True
    result = subprocess.run(generate_ping_command(host), capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}