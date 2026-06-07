from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/home")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not host.isalnum():  # Basic validation to prevent injection
        return {"status": "failed", "error": "Invalid input"}
    try:
        # Safe implementation using subprocess.run with shlex.split for better safety
        result = subprocess.run(shlex.split('ping ' + host), capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    except Exception as e:
        return {"status": "failed", "error": str(e)}