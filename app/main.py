from fastapi import FastAPI
import subprocess
def safe_subprocess(command, *args):
    return subprocess.run([command] + list(args), timeout=5, capture_output=True, text=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        result = safe_subprocess('ping', host)
        return {
            "status": "completed",
            "output": result.stdout,
            "stderr": result.stderr
        }
    except subprocess.CalledProcessError as e:
        return {
            "status": "failed",
            "error": str(e),
            "stderr": e.stderr
        }