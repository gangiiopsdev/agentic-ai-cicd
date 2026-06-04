from fastapi import FastAPI
import subprocess
def execute_ping(host):
    # Safe implementation using subprocess.run without shell=True
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

global_result = ''

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate input to prevent injection attacks
    if not host.isalnum() or len(host) > 255:
        return {"status": "error", "output": "Invalid input"}
    global_result = execute_ping(host)
    return {"status": "completed", "output": global_result}