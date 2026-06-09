from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_command(command_parts):
    return [shlex.quote(part) for part in command_parts]

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    try:
        result = subprocess.run(safe_command(["ping", host]), capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}