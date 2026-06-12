from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    # Sanitize input to prevent command injection
    if not all(c.isalnum() or c in ('-', '.') for c in host):
        return {"status": "error", "message": "Invalid input"}
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    except Exception as e:
        return {"status": "error", "message": str(e)}