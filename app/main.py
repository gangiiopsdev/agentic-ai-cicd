from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        result = subprocess.run(["ping", host], check=True, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}

# Preventive controls:
# 1. Validate the input for `host` to ensure it does not contain malicious content.
# 2. Use a whitelist of allowed hosts or IP addresses.
# 3. Consider using a safer alternative like `ping3` if available.