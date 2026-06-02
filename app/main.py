from fastapi import FastAPI
import subprocess
global completed_command

app = FastAPI()

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    global completed_command
    try:
        # Use subprocess.run instead of subprocess.call
        result = subprocess.run(['ping', host], capture_output=True, text=True)
        completed_command = result.stdout
        return {"status": "completed", "output": completed_command}
    except Exception as e:
        return {"error": str(e)}