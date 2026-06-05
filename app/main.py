from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if host in ['127.0.0.1', '::1']:  # Allow only localhost ping for demonstration purposes
        command = ["ping", host]
        result = subprocess.run(command, capture_output=True, text=True, check=False)
        return result.stdout
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    output = safe_ping(host)
    return {"status": "completed", "output": output}