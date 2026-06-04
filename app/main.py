from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Enhanced input validation and sanitization
    if not re.match(r'^[a-zA-Z0-9.-]{1,255}$', host):
        return {"status": "failed", "error": "Invalid input"}
    try:
        command = shlex.split(f'ping {host}')
        result = subprocess.run(command, capture_output=True, text=True, check=False)
        return {
            "status": "completed",
            "output": result.stdout,
            "stderr": result.stderr
        }
    except Exception as e:
        return {"status": "failed", "error": str(e)}