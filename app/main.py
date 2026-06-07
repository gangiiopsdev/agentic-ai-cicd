from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate host input to prevent injection attacks
    if not is_valid_host(host):
        return {"status": "error", "message": "Invalid host provided"}
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}

def is_valid_host(host: str) -> bool:
    # Add validation logic here, e.g., regex to check for allowed characters
    return all(c.isalnum() or c in ['.', '-'] for c in host)