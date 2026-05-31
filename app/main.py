from fastapi import FastAPI
import subprocess
def safe_getinput(command):
    return subprocess.run(command.split(), capture_output=True, text=True).stdout

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    result = safe_getinput(f'ping -c 4 {host}')
    return {"status": "completed", "result": result}