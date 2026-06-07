from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the host input to ensure it's safe to use in a subprocess command
    if not host.replace('.', '').replace('-', '').isalnum():
        return {"status": "failed", "error": "Invalid host format"}
    try:
        result = subprocess.run(['ping', host], check=True, text=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}