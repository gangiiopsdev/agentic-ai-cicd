from fastapi import FastAPI
import subprocess
import shlex
class SafeSubprocess:
    def run(self, command):
        try:
            result = subprocess.run(command, capture_output=True, text=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return e.stderr

app = FastAPI()
safe_subprocess = SafeSubprocess()

def ping(host: str):
    # Validate input to prevent command injection
    if not host.isalnum():
        raise ValueError("Invalid input")
    command = ['ping', '-c', '1'] + shlex.split(host)
    response = safe_subprocess.run(command)
    return {"status": "completed", "output": response}

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_safe(host: str):
    # Validate input to prevent command injection
    if not host.isalnum():
        raise ValueError("Invalid input")
    command = ['ping', '-c', '1'] + shlex.split(host)
    response = safe_subprocess.run(command)
    return {"status": "completed", "output": response}