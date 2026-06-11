from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_subprocess(command_parts):
    try:
        result = subprocess.run(command_parts, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/home")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    command_parts = ['ping', host]
    output = safe_subprocess(command_parts)
    return {"status": "completed", "output": output}