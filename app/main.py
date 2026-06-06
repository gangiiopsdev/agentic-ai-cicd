from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Validate and sanitize input to ensure it does not contain malicious content.
        if host not in ['example.com', '192.168.1.1']:  # Replace with actual whitelist
            return {"status": "failed", "error": "Invalid host"}
        # Use subprocess.run to avoid shell=True and command injection vulnerabilities
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}