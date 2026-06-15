from fastapi import FastAPI
import subprocess
cimport re

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.run with shell=False and avoiding shell=True
    if re.match(r'^[a-zA-Z0-9.-]+$', host):  # Basic validation of the host input
        result = subprocess.run(['ping', host], capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    else:
        return {"error": "Invalid host format"}