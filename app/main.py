from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    allowed_hosts = ["example.com", "test.example.com"]  # Define a whitelist of allowed hosts
    if host not in allowed_hosts:
        return {"status": "error", "message": "Host is not allowed to be pinged"}
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "message": str(e)}

# Preventive controls
# 1. Validate input to ensure it does not contain malicious commands.
# 2. Use a whitelist of allowed hosts or services to ping.
# 3. Consider using a more secure method for network diagnostics if possible.