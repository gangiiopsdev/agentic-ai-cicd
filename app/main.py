from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Sanitize the input to prevent command injection
        if not host.isalnum() or len(host) > 255:
            raise ValueError("Invalid host")
        output = subprocess.check_output(['ping', '-c', '1', host], timeout=5, stderr=subprocess.STDOUT)
        return {"status": "completed", "output": output.decode('utf-8')}
    except Exception as e:
        return {"status": "failed", "error": str(e)}