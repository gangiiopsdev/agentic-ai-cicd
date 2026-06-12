from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the input
    if not host.strip() or len(host) > 100:
        return {"error": "Invalid host provided"}
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    except Exception as e:
        return {"error": str(e)}