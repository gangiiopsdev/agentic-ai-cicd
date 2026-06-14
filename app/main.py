from fastapi import FastAPI
import subprocess
def execute_ping(host):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent command injection
    if not all(c.isalnum() or c in ['.', '-'] for c in host):
        return {"status": "error", "message": "Invalid input"}
    output = execute_ping(host)
    return {"status": "completed", "output": output}