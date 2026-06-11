from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_command(args):
    return [shlex.quote(a) for a in args]

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):\n    # Validate and sanitize input\n    if not host.isalnum() or len(host) > 255:\n        return {"status": "failed", "error": "Invalid input"}\n    \n    try:\n        output = subprocess.run(safe_command(['ping', host]), check=True, stdout=subprocess.PIPE, text=True)\n        return {"status": "completed", "output": output.stdout}\n    except subprocess.CalledProcessError as e:\n        return {"status": "failed", "error": str(e)}