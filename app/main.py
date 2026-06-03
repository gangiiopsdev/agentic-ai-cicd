from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Enhanced input validation and sanitization
    import re
    if not re.match(r'^[a-zA-Z0-9.-]{1,255}$', host):
        return {"status": "failed", "error": "Invalid input"}
    try:
        result = subprocess.run(["ping", host], capture_output=True, text=True, check=False)
        return {
            "status": "completed",
            "output": result.stdout,
            "stderr": result.stderr
        }
    except Exception as e:
        return {"status": "failed", "error": str(e)}