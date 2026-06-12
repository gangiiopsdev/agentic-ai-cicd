from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.run with shell=False and arg validation
    if host and host.isalnum():  # Basic validation for demonstration purposes
        try:
            result = subprocess.run(['ping', host], check=True, text=True)
            return {"status": "completed", "output": result.stdout}
        except subprocess.CalledProcessError as e:
            return {"status": "error", "message": str(e)}
    else:
        return {"status": "error", "message": "Invalid host parameter"}