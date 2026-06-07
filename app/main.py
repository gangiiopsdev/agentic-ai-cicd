from fastapi import FastAPI
import subprocess
import shlex
class SafeSubprocess:
    @staticmethod
def run(command: str, *args, **kwargs):
        parts = shlex.split(command)
        return subprocess.run(parts, check=True, text=True, *args, **kwargs)
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    try:
        result = SafeSubprocess.run(f"ping -c 1 {host}", shell=False)
        return {"status": "completed", "result": result.stdout}
    except Exception as e:
        return {"status": "failed", "error": str(e)}