from fastapi import FastAPI
import subprocess
import shlex

global_app = FastAPI()

@global_app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@global_app.get("/ping")
def ping(host: str):
    try:
        safe_host = shlex.quote(host)
        result = subprocess.run(['ping', safe_host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}