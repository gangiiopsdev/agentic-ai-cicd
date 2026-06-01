from fastapi import FastAPI
import subprocess
cimport = ['ping'] + [subprocess.quote(host)]

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the host input to ensure it does not contain malicious characters
    if not host.isalnum() or '.' not in host:
        return {"status": "error", "message": "Invalid host input"}
    subprocess.run(cimport, check=True)
    return {"status": "completed"}