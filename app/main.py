from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the input
    if not host.strip() or any(char in host for char in ' ;&*!$%^`~{}[]|\:\"<>',.?/~'):  # Example of basic validation
        return {"status": "error", "message": "Invalid host provided"}
    try:
        # Safer implementation using list for subprocess arguments
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "message": e.stderr}