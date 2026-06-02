from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def safe_call(command):
        return subprocess.run(shlex.split(command), capture_output=True, text=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the input to prevent command injection
    if not host.isalnum():
        return {"status": "error", "output": "Invalid input"}
    command = f'ping {host}'
    result = SafePing.safe_call(command)
    return {"status": "completed", "output": result.stdout}