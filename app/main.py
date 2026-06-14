from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

class SafeSubprocess:
    @staticmethod
def check_output(command: list) -> str:
        try:
            result = subprocess.run(command, capture_output=True, text=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return f'Failed to execute command: {e.stderr}'

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the host input to ensure it only contains allowed characters
    if not all(c.isalnum() or c in '.-' for c in host):
        return {"status": "error", "message": "Invalid hostname"}
    safe_host = subprocess.quote(host)
    command = ['ping', safe_host]
    output = SafeSubprocess.check_output(command)
    return {"status": "completed", "output": output}