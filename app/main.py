from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/"),
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate or escape the host input
    if not is_valid_host(host):
        return {"status": "failed", "error": "Invalid host"}
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}

# Define a function to validate or escape the host input
def is_valid_host(host: str) -> bool:
    # Implement validation logic here, e.g., check for allowed characters and format
    return all(char.isalnum() or char in ['-', '.'] for char in host)