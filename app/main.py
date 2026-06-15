from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}

# Preventive Controls
# 1. Validate and sanitize input to ensure it does not contain malicious content.
# 2. Use a whitelist of allowed hosts or IP addresses.
# 3. Avoid using subprocess when possible, consider alternative libraries for similar tasks.