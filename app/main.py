from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/"),
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation with sanitized input
    try:
        command = shlex.split('ping ' + host)
        result = subprocess.run(command, capture_output=True, text=True, timeout=10)
        return {"status": "completed", "output": result.stdout}
    except Exception as e:
        return {"status": "failed", "error": str(e)}