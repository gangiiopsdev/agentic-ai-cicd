from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/"),
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    try:
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "message": str(e)}

# Preventive controls
# 1. Validate input to ensure it only contains allowed characters (e.g., alphanumeric and a few specific symbols)
# 2. Use a whitelist of allowed hosts or domains
# 3. Consider using an alternative approach that does not involve subprocess for security reasons