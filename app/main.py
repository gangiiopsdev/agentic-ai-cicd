from fastapi import FastAPI
import subprocess
def execute_ping(host):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    # Validate host input
    if not host.isalnum() or len(host) > 64:
        return {"status": "error", "result": "Invalid host input"}
    result = execute_ping(host)
    return {"status": "completed", "result": result}