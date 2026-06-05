from fastapi import FastAPI
import subprocess
def validate_host(host: str) -> bool:
    return host.isalnum() and len(host) <= 255

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {"status": "failed", "error": "Invalid input"}
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}

# Recommended changes to mitigate the vulnerability:
# - Use a whitelist of allowed hosts instead of alphanumeric validation.
# - Sanitize and validate the host input more strictly.