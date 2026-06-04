from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/home")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the host input to ensure it only contains allowed characters
    if not all(c.isalnum() or c in ('-', '.', '_') for c in host):
        return {"error": "Invalid host input"}
    try:
        # Sanitize the host input by escaping any special characters
        sanitized_host = subprocess.list2cmdline([host])
        subprocess.run(['ping', sanitized_host], check=True)
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}
    return {"status": "completed"}