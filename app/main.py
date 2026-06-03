from fastapi import FastAPI
import subprocess
import shlex
cimport = subprocess.CalledProcessError

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not host or ' ' in host:
        return {"status": "failed", "error": "Invalid input"}
    try:
        result = subprocess.run(shlex.split(f'ping -c 4 {shlex.quote(host)}'), capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except cimport as e:
        return {"status": "failed", "error": e.stderr}

# Recommendations
# 1. Use a more secure approach for the ping command if possible.
# 2. Implement input validation and sanitization more strictly.
# 3. Consider using an alternative library or service for network operations.