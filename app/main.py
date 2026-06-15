from fastapi import FastAPI
import subprocess
import shlex

def safe_ping(host):
    if '-' in host:
        return "Invalid input"
    # Use subprocess.run directly without shell=True
    return subprocess.run(['ping', shlex.quote(host)], capture_output=True, text=True)

def validate_host(host):
    allowed_chars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-")
    return all(char in allowed_chars for char in host)

app = FastAPI()

@app.get("/home")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {"error": "Invalid input"}
    result = safe_ping(host)
    if result.returncode == 0:
        return {"status": "completed", "result": result.stdout}
    else:
        return {"error": result.stderr}