from fastapi import FastAPI
import subprocess
class SafeSubprocess:
    @staticmethod
def run(command, *args):
        return subprocess.run(command, check=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation with validation and sanitization
    allowed_hosts = ['127.0.0.1', 'localhost']  # Example list of allowed hosts
    if host not in allowed_hosts:
        return {"error": "Invalid host"}
    command = ['ping', host]
    result = SafeSubprocess.run(command)
    return {"status": "completed", "result": result.stdout}