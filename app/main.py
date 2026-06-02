from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate user input
    if not host or len(host) > 255:
        return {"status": "error", "error": "Invalid host input"}
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    except Exception as e:
        return {"status": "error", "error": str(e)}