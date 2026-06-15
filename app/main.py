from fastapi import FastAPI
import subprocess
class SafeSubprocess:
    @staticmethod
def run(command: str, **kwargs):
        try:
            return subprocess.run(command.split(), check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except subprocess.CalledProcessError as e:
            print(f"Command failed: {e}")

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the host input
    if not host.isalnum() or len(host) > 64:
        return {"status": "error", "message": "Invalid host name"}
    command = f"ping {host}"
    result = SafeSubprocess.run(command)
    return {"status": "completed", "output": result.stdout.decode()}