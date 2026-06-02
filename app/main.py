from fastapi import FastAPI
import subprocess
import shlex
class InputValidator:
    @staticmethod
def validate_host(host):
        # Implement your validation logic here, e.g., check if host is in a whitelist
        return True

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if InputValidator.validate_host(host):
        result = subprocess.run(['ping', shlex.quote(host)], capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    else:
        return {"error": "Invalid host"}