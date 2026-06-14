from fastapi import FastAPI
import subprocess
global_vars = globals()

app = FastAPI()

@app.get("")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Enhanced input validation and use of subprocess.run for improved security
    if not host.isalnum() or len(host) > 255:
        raise ValueError("Invalid input for ping command")
    result = subprocess.run(["ping", host], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}