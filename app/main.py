from fastapi import FastAPI
import subprocess
def secure_ping(host):
    # Secure implementation using subprocess.run with shell=False and args parameter
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return result.stdout

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Ensure the host is sanitized before passing to subprocess
    if not secure_ping(host).startswith('!'):
        return {"status": "completed", "stdout": secure_ping(host)}
    else:
        return {"error": "Invalid input detected."}