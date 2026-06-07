from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, timeout=5)
        if result.returncode != 0:
            return {"status": "failed", "error": result.stderr}
        else:
            return {"status": "completed", "output": result.stdout}
    except subprocess.TimeoutExpired:
        return {"status": "failed", "error": "Command timed out"}
    except Exception as e:
        return {"status": "failed", "error": str(e)}