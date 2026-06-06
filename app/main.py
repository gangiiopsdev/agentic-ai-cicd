from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    args = ['ping', '-c', '1', host]
    result = subprocess.run(args, capture_output=True, text=True, check=False)
    return result.stdout, result.stderr
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    if not host.isalnum():
        return {"status": "failed", "error": "Invalid input"}
    stdout, stderr = safe_ping(host)
    if stderr:
        return {"status": "failed", "error": stderr}
    return {"status": "completed", "output": stdout}